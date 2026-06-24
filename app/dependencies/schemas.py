from enum import Enum
from pydantic import BaseModel, Field


class ComplaintType(str, Enum):
    customer_service = "customer_service"
    product_quality = "product_quality"
    billing_and_payment = "billing_and_payment"
    food_and_dining = "food_and_dining"
    shipping_and_delivery = "shipping_and_delivery"
    online_experience = "online_experience"
    other = "other"


class GenerateComplaintRequest(BaseModel):
    company_name: str = Field(..., min_length=1, max_length=200)
    complaint_body: str = Field(..., min_length=10, max_length=5000)
    complaint_type: ComplaintType = ComplaintType.customer_service
    karen_level: int = Field(default=0, ge=0, le=5)


class GenerateComplaintResponse(BaseModel):
    complaint: str
    karen_level: int
    company_name: str
