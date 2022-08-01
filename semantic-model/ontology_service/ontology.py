import datetime
import enum

from functools import partial
from typing import List

from owlready2 import owlready2
from owlready2 import get_ontology
from owlready2 import Imp
from owlready2 import destroy_entity
from owlready2 import sync_reasoner_pellet
from pydantic import BaseModel, create_model

from importlib import resources
from . import owl
from .util import camel_to_snake
from .models import Field, Soil, Plant

from .swrl_rules import SWRL_RULES

owlready2.namespace.set_log_level(1)

# TODO make ontology available via http
onto_cassava = get_ontology("file://" +
                            str(resources.path(owl, "cassava-disease.owl"))
                            ).load(reload=True)
# converted sosa to rdf/xml since there it can not be loaded by
# owlready2 directly at the moment
sosa = get_ontology("file://" +
                    str(resources.path(owl, "sosa.owl"))
                    ).load()
onto_cassava.imported_ontologies.append(sosa)

observable_properties = {camel_to_snake(i.name):
                             i.name for i in sosa.ObservableProperty.instances()}

diseases = onto_cassava.PlantDisease.instances()

_possible_conditions = {camel_to_snake(disease.name):
                            [] for disease in diseases}
for condition in onto_cassava.DiseaseCondition.instances():
    disease = condition.enablesDisease
    _possible_conditions[camel_to_snake(disease.name)].append(condition)

nums_conditions_for_disease = {}


class Observation(BaseModel):
    timestamp: datetime.datetime
    value: float
    observed_property: enum.Enum(
        'ObservableProperties',  # noqa
        observable_properties,
        type=str
    )


class DiseaseVectorEntry(BaseModel):
    probability: float = 0
    symptoms: str = "No visual symptoms"
    explanations: List[str] = []


_model_dict = {camel_to_snake(disease.name):
                   (DiseaseVectorEntry, ...) for disease in diseases}
_model_dict['healthy'] = (DiseaseVectorEntry, ...)
DiseaseVector = create_model('DiseaseVector', **_model_dict)


def _test_data_setup():
    with onto_cassava:
        for i in range(1, 6):
            field = onto_cassava.Field(f"field_{i}")
            field.hasRainySeason = False
            soil = onto_cassava.Soil(f"soil_{i}")
            soil.isPartOfField = field
            plant = onto_cassava.Plant(f"plant_{i}")
            plant.isPlantedIn = soil

        onto_cassava["field_1"].hasRainySeason = True


_test_data_setup()


def _load_swrl_rules():
    with onto_cassava:
        for disease in SWRL_RULES:
            for rule_string in SWRL_RULES[disease].values():
                imp = Imp()
                imp.set_as_rule(rule_string, namespaces=[onto_cassava, sosa])


# def _create_rule(rule_string: str):
#     with onto_cassava:
#         imp = Imp()
#         imp.set_as_rule(rule_string)


_load_swrl_rules()
sync_reasoner_pellet(infer_property_values=True,
                     infer_data_property_values=True)


def add_observation(feature_of_interest: str,
                    feature_of_interest_id: int,
                    observation: Observation):
    feature = _get_individual(feature_of_interest, feature_of_interest_id)
    observed_property = onto_cassava[observation.observed_property.value]

    with onto_cassava:
        # remove older observations of the same type
        old_observations = filter(partial(_observation_is_old,
                                          feature,
                                          observed_property),
                                  sosa.Observation.instances())
        for entity in old_observations:
            destroy_entity(entity)

        obs = sosa.Observation()
        obs.observedProperty.append(observed_property)
        obs.hasFeatureOfInterest.append(feature)
        obs.hasSimpleResult.append(observation.value)
        obs.resultTime.append(observation.timestamp)


def _observation_is_old(feature: owlready2.individual,
                        observed_property: owlready2.individual,
                        observation: owlready2.individual):
    return observation.hasFeatureOfInterest[0] == feature \
           and observation.observedProperty[0] == observed_property


def _get_individual(type_name: str, id: int):
    name = f"{type_name}_{id}"
    instance = onto_cassava[name]
    if instance is not None:
        return instance
    else:
        raise KeyError("No individual named {name} found.")


def _individual_id(individual: owlready2.individual):
    return individual.name.split('_')[1]


def get_soil(id: int):
    soil = _get_individual('soil', id)
    field = _individual_id(soil.isPartOfField)
    plants = list(map(_individual_id, soil.hasPlant))
    return Soil(id=id, field=field, plants=plants)


def get_field(id: int):
    field = _get_individual('field', id)
    soils = list(map(_individual_id, field.hasSoil))
    return Field(id=id, rainy_season=field.hasRainySeason, soils=soils)


def get_plant(id: int):
    plant = _get_individual('plant', id)
    soil = _individual_id(plant.isPlantedIn)
    return Plant(id=id, soil=soil)


def get_all_fields():
    ids = map(_individual_id, onto_cassava.Field.instances())
    return list(map(get_field, ids))


def get_all_soils():
    ids = map(_individual_id, onto_cassava.Soil.instances())
    return list(map(get_soil, ids))


def get_all_plants():
    ids = map(_individual_id, onto_cassava.Plant.instances())
    return list(map(get_plant, ids))


def _get_explanations(conditions):
    return [str(condition.definition[0]) for condition in conditions]


def calculate_disease_vector(plant_id: int):
    plant = _get_individual('plant', plant_id)

    plant.hasCondition = []
    with onto_cassava:
        sync_reasoner_pellet(infer_property_values=True,
                             infer_data_property_values=True)

    found_conditions = plant.hasCondition
    total_possible_conditions = len(onto_cassava.DiseaseCondition.instances())

    disease_vector = {}
    for disease in diseases:
        conditions_for_disease = list(
            filter(lambda c: c.enablesDisease == disease, found_conditions))
        num_possible_conditions = \
            len(_possible_conditions[camel_to_snake(disease.name)])
        if num_possible_conditions > 0:
            probability = len(conditions_for_disease) / num_possible_conditions
        else:
            probability = 0

        disease_vector[camel_to_snake(disease.name)] = {
            'symptoms': str(disease.hasSymptoms[0].definition[0]),
            'explanations': _get_explanations(conditions_for_disease),
            'probability': probability
        }

    disease_vector['healthy'] = \
        {'probability':
             1 - (len(found_conditions) / total_possible_conditions)}

    return DiseaseVector.parse_obj(disease_vector)
