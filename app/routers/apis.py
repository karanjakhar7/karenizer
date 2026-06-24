from fastapi import APIRouter, HTTPException
from ..dependencies.schemas import GenerateComplaintRequest, GenerateComplaintResponse
from ..services.complaint_generator import generate_karen_complaint

router = APIRouter(prefix="/api")


@router.post("/generate", response_model=GenerateComplaintResponse)
async def generate_complaint(data: GenerateComplaintRequest):
    try:
        complaint = await generate_karen_complaint(
            company_name=data.company_name,
            complaint_body=data.complaint_body,
            complaint_type=data.complaint_type.value,
            karen_level=data.karen_level,
        )
        return GenerateComplaintResponse(
            complaint=complaint,
            karen_level=data.karen_level,
            company_name=data.company_name,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
