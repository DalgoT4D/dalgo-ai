from fastapi import APIRouter
from mindsdb_operations.initial_config import ModelDetails
from mindsdb_operations.models_fn import models_fn as get_models


router = APIRouter()


@router.post("/api/mindsdb/classifier/models")
async def models(item: ModelDetails):
    try:
        outcome = get_models(item)
        return {"status": "success", "outcome": str(outcome)}
    except Exception as e:
        print(e)
        return {"status": "failed", "outcome": str(e)}
