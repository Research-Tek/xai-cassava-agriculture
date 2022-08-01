from fastapi import FastAPI
from .routers import soils, plants, fields

api = FastAPI(title="CassavaDiseaseOntologyService")

tags_metadata = [
    {
        "name": "soils",
        "description": "Endpoint to submit soil measurements",
    },
]

api.include_router(fields.router)
api.include_router(soils.router)
api.include_router(plants.router)
