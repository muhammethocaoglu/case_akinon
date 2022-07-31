import json

from src.api.handler.error_response import ErrorResponse
from src.infra.util.errors import errors


def generate_unprocessable_entity_error_response(error_code=1100):
    return {
        "application/json": {
            "example": json.dumps(
                ErrorResponse(
                    error_code=error_code, error_message=errors[error_code]
                ).dict()
            )
        }
    }
