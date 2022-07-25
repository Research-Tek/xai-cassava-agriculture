import asyncio
import logging
import os
import sys
import time
from typing import List
from urllib.parse import urljoin
import numpy as np

from fastapi import FastAPI, File, HTTPException
import requests
from pydantic import BaseModel

api = FastAPI(title="CassavaDiseaseDecisionService")

try:
    ONTO_URL = os.environ['ONTOLOGY_SERVICE_URL']
    CLASSIFIER_URL = os.environ['CLASSIFIER_SERVICE_URL']
except KeyError as e:
    logging.error(f"Envrionment variable {str(e)} needs to be set.")
    sys.exit(1)


class DiseasePrediction(BaseModel):
    disease: str
    explanations: List[str]
    visual_certainty: float
    knowledge_certainty: float
    image_classification_time: float
    reasoner_time: float


@api.post("/plants/{plant_id}/predict-disease", response_model=DiseasePrediction)
async def predict_disease(plant_id, image: bytes = File(...)):
    image_task = asyncio.create_task(get_image_classification(image))
    onto_task = asyncio.create_task(get_ontology_disease_vector(plant_id))

    try:
        image_vector, image_time = await image_task
        ontology_vector, onto_time = await onto_task
    except requests.exceptions.ConnectionError as ex:
        raise HTTPException(status_code=500, detail=str(ex))

    voted_disease = majority_vote(image_vector,
                                  {disease: ontology_vector[disease]['probability']
                                   for disease in ontology_vector})

    visual_certainty = image_vector[voted_disease]
    knowledge_certainty = ontology_vector[voted_disease]['probability']

    explanations = ontology_vector[voted_disease]['explanations']

    if visual_certainty >= 0.5:
        healthy_phrase = " no" if voted_disease == 'healthy' else ""
        explanations.append(f'Plant shows{healthy_phrase} visual symptoms.')

    return DiseasePrediction(disease=voted_disease,
                             explanations=explanations,
                             visual_certainty=visual_certainty,
                             knowledge_certainty=knowledge_certainty,
                             image_classification_time=image_time,
                             reasoner_time=onto_time)


async def get_image_classification(image):
    start_time = time.time()
    headers = {'accept': 'application/json'}
    r = requests.post(urljoin(CLASSIFIER_URL, '/predict_image'), files={'file': image}, headers=headers)
    r.raise_for_status()
    end_time = time.time()
    return r.json()['disease_prediction'], end_time - start_time


async def get_ontology_disease_vector(plant_id):
    start_time = time.time()
    headers = {'accept': 'application/json'}
    r = requests.get(urljoin(ONTO_URL, f'/plants/{plant_id}/disease-vector'), headers=headers)
    r.raise_for_status()
    end_time = time.time()
    return r.json(), end_time - start_time

def majority_vote(image_vector, ontology_vector):
    diseases = ontology_vector.keys()
    image_probs = [image_vector[disease] for disease in diseases]
    ontology_probs = [ontology_vector[disease] for disease in diseases]

    prediction = np.average([image_probs, ontology_probs], axis=0, weights=[1.0, 1.2])

    return list(diseases)[np.argmax(prediction)]

