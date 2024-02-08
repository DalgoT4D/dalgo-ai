from fastapi import APIRouter
from mindsdb_operations.initial_config import ModelDetails
from mindsdb_operations.models_fn import models_fn


router = APIRouter()


@router.post("/api/mindsdb/classifier/models")
def models(item: ModelDetails):
    try:
        outcome = models_fn(item)
        return {"status": "success", "outcome": str(outcome)}
    except Exception as e:
        return {"status": "failed", "outcome": str(e)}
