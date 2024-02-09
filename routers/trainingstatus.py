from fastapi import APIRouter
from mindsdb_operations.initial_config import TrainingStatusDetails
from mindsdb_operations.training_status_fn import training_status_fn as training_status


router = APIRouter()


@router.post("/api/mindsdb/classifier/trainingstatus")
async def training_status_of_model(item: TrainingStatusDetails):
    try:
        outcome = training_status(item)
        return {"status": "success", "outcome": outcome}
    except Exception as e:
        print(e)
        return {"status": "failed", "outcome": str(e)}
