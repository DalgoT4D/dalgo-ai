from fastapi import APIRouter
from mindsdb_operations.initial_config import TrainDetails
from mindsdb_operations.train_fn import train_fn


router = APIRouter()


@router.post("/api/mindsdb/classifier/train")
def train_fn(item: TrainDetails):
    try:
        outcome = train_fn(item)
        return {"status": "success", "outcome": str(outcome)}
    except Exception as e:
        return {"status": "failed", "outcome": str(e)}
