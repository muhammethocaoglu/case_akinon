import logging
import traceback
from typing import Dict, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse

from src.api.handler.error_response import ErrorResponse
from src.infra.exception.bad_request_exception import BadRequestException
from src.infra.exception.infra_exception import InfraException
from src.infra.util.errors import errors


def unhandled_exception_handler(request, exc: Exception):
    error_code = 1999
    logging.exception(msg=generate_error_message(error_code))
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=generate_error_content(error_code=error_code),
    )


def validation_exception_handler(request, exc: RequestValidationError):
    error_code = 1000
    logging.error(msg=generate_error_message(error_code))
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=generate_error_content(
            error_code=error_code, error_detail=exc.errors()
        ),
    )


def infra_exception_handler(request, exc: InfraException):
    logging.exception(generate_error_message(exc.error_code))
    return generate_json_response(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        error_code=exc.error_code,
        error_detail=exc.error_detail,
    )


def bad_request_exception_handler(request, exc: BadRequestException):
    logging.exception(generate_error_message(exc.error_code))
    return generate_json_response(
        status_code=status.HTTP_400_BAD_REQUEST,
        error_code=exc.error_code,
        error_detail=exc.error_detail,
    )


def generate_json_response(
    status_code: int, error_code: int, error_detail: Optional[Dict]
):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(
            ErrorResponse(
                error_code=error_code,
                error_message=errors[error_code],
                error_detail=[error_detail] if error_detail else None,
            ).dict()
        ),
    )


def generate_error_message(error_code):
    return "error code: {}, error message: {}".format(error_code, errors[error_code])


def generate_stack_trace(exc: Exception) -> str:
    return "".join(traceback.TracebackException.from_exception(exc).format())


def generate_error_content(error_code: int, error_detail: list = []):
    return jsonable_encoder(
        ErrorResponse(
            error_code=error_code,
            error_message=errors[error_code],
            error_detail=error_detail,
        ).dict()
    )
