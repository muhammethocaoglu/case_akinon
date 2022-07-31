from typing import List

from fastapi import APIRouter, Depends, Query
from starlette import status

from src.api.controller.dto.exchange_rate_output_dto import ExchangeRateOutputDto
from src.api.controller.service_resolver import (
    get_exchange_rate_service,
)
from src.api.handler.error_response import ErrorResponse, generate_error_response
from src.core.model.retrieve_exchange_rates_input_model import (
    RetrieveExchangeRatesInputModel,
)
from src.core.model.retrieve_exchange_rates_output_model import (
    RetrieveExchangeRateOutputModel,
)

router = APIRouter()


@router.get(
    "",
    response_model=List[ExchangeRateOutputDto],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": List[ExchangeRateOutputDto]},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ErrorResponse,
            "content": generate_error_response(),
        },
    },
)
def retrieve_exchange_rates(
    source_currency: str = Query(default="EUR"),
    target_currency_list: List[str] = Query(default=[]),
    exchange_rate_service=Depends(get_exchange_rate_service),
):
    exchange_rates: List[
        RetrieveExchangeRateOutputModel
    ] = exchange_rate_service.retrieve_exchange_rates(
        RetrieveExchangeRatesInputModel(
            source_currency=source_currency, target_currency_list=target_currency_list
        )
    )

    return [
        ExchangeRateOutputDto(**exchange_rate_item.dict())
        for exchange_rate_item in exchange_rates
    ]
