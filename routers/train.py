from fastapi import APIRouter
from mindsdb_operations.initial_config import TrainDetails
from mindsdb_operations.train_fn import train_fn as train_model


router = APIRouter()


@router.post("/api/mindsdb/classifier/train")
async def train_fn(item: TrainDetails):
    try:
        outcome = train_model(item)
        return {"status": "success", "outcome": outcome}
    except Exception as e:
        print(e)
        return {"status": "failed", "outcome": str(e)}
