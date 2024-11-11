from fastapi import UploadFile, File
from pydantic import BaseModel, Field
from enum import Enum
from typing import Literal, Optional

class ComplaintType(Enum):
    customer_service = "customer_service"
    product_quality = "product_quality"
    billing_and_payment = "billing_and_payment"


class GenerateComplaintRequest(BaseModel):
    company_name: str
    complaint_body: str
    complaint_type: Optional[ComplaintType] = Field(default=ComplaintType.customer_service)
    karen_level: int = Field(default=0, ge=0, le=5)
    file: Optional[UploadFile] = File(...)
