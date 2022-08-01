from typing import List

from pydantic import BaseModel


class IndividualModel(BaseModel):
    id: int


class Field(IndividualModel):
    rainy_season: bool
    soils: List[int]


class Soil(IndividualModel):
    field: int
    plants: List[int]


class Plant(IndividualModel):
    soil: int
