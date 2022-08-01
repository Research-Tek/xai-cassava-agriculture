from typing import List

from fastapi import APIRouter, HTTPException

from ..models import Soil
from ..ontology import add_observation, get_all_soils
from ..ontology import get_soil
from ..ontology import Observation

router = APIRouter()


@router.get("/soils/{soil_id}",
            response_model=Soil,
            status_code=200,
            tags=["soils"])
async def read_soil(soil_id: int):
    try:
        soil = get_soil(soil_id)
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Soil with id {soil_id} not found.")
    return soil


@router.get("/soils",
            response_model=List[Soil],
            status_code=200,
            tags=["soils"])
async def read_all_soils():
    return get_all_soils()


@router.post("/soils/{soil_id}/observations",
             response_model=Observation,
             status_code=201,
             tags=["soils"])
async def create_soil_observation(observation: Observation, soil_id: int):
    try:
        add_observation('soil', soil_id, observation)
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Soil with id {soil_id} not found.")
    return observation
