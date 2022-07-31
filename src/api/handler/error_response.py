from typing import Optional

from pydantic.main import BaseModel


def generate_error_response():
    return {
        "application/json": {
            "example": ErrorResponse(
                error_code=10, error_message="Cannot get expected response"
            ).dict()
        }
    }


class ErrorResponse(BaseModel):
    error_code: Optional[int]
    error_message: Optional[str]
    error_detail: Optional[list]
