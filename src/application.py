from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from src.api.controller import exchange_rate_controller, exchange_controller
from src.api.handler.exception_handler import (
    validation_exception_handler,
    unhandled_exception_handler,
    infra_exception_handler, bad_request_exception_handler,
)
from src.infra.exception.bad_request_exception import BadRequestException
from src.infra.exception.infra_exception import InfraException


def create_app():
    app = FastAPI(
        title="Finance API",
        description="This api is for managing exchange",
        version="0.1.0",
        openapi_url="/openapi.json",
        docs_url="/",
        redoc_url="/redoc",
    )

    app.add_exception_handler(Exception, unhandled_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(InfraException, infra_exception_handler)
    app.add_exception_handler(BadRequestException, bad_request_exception_handler)

    app.include_router(
        exchange_rate_controller.router,
        prefix="/api/v1/exchange-rates",
        tags=["exchange-rate"],
    )

    app.include_router(
        exchange_controller.router,
        prefix="/api/v1/exchanges",
        tags=["exchange"],
    )
    return app
