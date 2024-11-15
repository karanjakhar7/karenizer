from fastapi import APIRouter
from ..dependencies.schemas import GenerateComplaintRequest
router = APIRouter()

# @router.get("/")
# async def root():
#     return {"message": "Hello World"}


@router.post("/generate_complaint")
async def generate_complaint(data: GenerateComplaintRequest):
    print(data.file.filename)
    return {"message": "Complaint generated"}

