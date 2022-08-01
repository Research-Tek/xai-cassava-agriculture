from typing import List

from fastapi import APIRouter, HTTPException

from ..models import Plant
from ..ontology import DiseaseVector, get_plant, get_all_plants
from ..ontology import calculate_disease_vector

router = APIRouter()


@router.get("/plants/{plant_id}",
            response_model=Plant,
            status_code=200,
            tags=["plants"])
async def read_plant(plant_id: int):
    try:
        plant = get_plant(plant_id)
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Plant with id {plant_id} not found.")
    return plant


@router.get("/plants",
            response_model=List[Plant],
            status_code=200,
            tags=["plants"])
async def read_all_plants():
    return get_all_plants()


@router.get("/plants/{plant_id}/disease-vector",
            response_model=DiseaseVector,
            status_code=200,
            tags=["plants"])
async def get_plant_disease_vector(plant_id: int):
    try:
        disease_vector = calculate_disease_vector(plant_id)
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Plant with id {plant_id} not found.")
    return disease_vector
