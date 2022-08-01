from typing import List

from fastapi import APIRouter, HTTPException

from ..models import Field
from ..ontology import add_observation
from ..ontology import Observation
from ..ontology import get_field, get_all_fields

router = APIRouter()


@router.get("/fields/{field_id}",
            response_model=Field,
            status_code=200,
            tags=["fields"])
async def read_field(field_id: int):
    try:
        field = get_field(field_id)
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Field with id {field_id} not found.")
    return field


@router.get("/fields",
            response_model=List[Field],
            status_code=200,
            tags=["fields"])
async def read_all_fields():
    return get_all_fields()


@router.post("/fields/{field_id}/observations",
             response_model=Observation,
             status_code=201,
             tags=["fields"])
async def create_field_observation(observation: Observation, field_id: int):
    try:
        add_observation('field', field_id, observation)
    except KeyError:
        raise HTTPException(status_code=404,
                            detail=f"Field with id {field_id} not found.")
    return observation
