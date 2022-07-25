from ontology_service import main
import uvicorn

if __name__ == "__main__":
    uvicorn.run(main.api, host="0.0.0.0", port=8001)
