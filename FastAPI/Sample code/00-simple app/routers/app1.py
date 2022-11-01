from fastapi import APIRouter

router = APIRouter(
    prefix="/app1",
    tags=["app1"]
)

@router.get('')
async def hello():
    return {"message":"Hello app1"}