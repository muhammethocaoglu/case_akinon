from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from src.api.controller.dto.create_exchange_input_dto import CreateExchangeInputDto
from src.api.controller.dto.create_exchange_output_dto import CreateExchangeOutputDto
from src.api.controller.dto.search_exchange_input_dto import SearchExchangeInputDto
from src.api.controller.dto.search_exchange_list_item_output_dto import (
    SearchExchangeListItemOutputDto,
)
from src.api.controller.service_resolver import (
    get_exchange_service,
)
from src.api.handler.error_response import ErrorResponse, generate_error_response
from src.core.model.create_exchange_input_model import CreateExchangeInputModel
from src.core.model.create_exchange_output_model import CreateExchangeOutputModel
from src.core.model.search_exchange_list_item_output_model import (
    SearchExchangeListItemOutputModel,
)
from src.core.service.exchange_service import ExchangeService

router = APIRouter()


@router.post(
    "",
    response_model=CreateExchangeOutputDto,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": CreateExchangeOutputDto},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ErrorResponse,
            "content": generate_error_response(),
        },
    },
)
def create(
    create_exchange_input_dto: CreateExchangeInputDto,
    exchange_service: ExchangeService = Depends(get_exchange_service),
):
    create_exchange_output_model: CreateExchangeOutputModel = exchange_service.create(
        CreateExchangeInputModel(**create_exchange_input_dto.dict())
    )

    return CreateExchangeOutputDto(**create_exchange_output_model.dict())


@router.get(
    "",
    response_model=List[SearchExchangeListItemOutputDto],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": List[SearchExchangeListItemOutputDto]},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": ErrorResponse,
            "content": generate_error_response(),
        },
    },
)
def search(
    search_exchange_input_dto: SearchExchangeInputDto = Depends(),
    exchange_service=Depends(get_exchange_service),
):
    search_result: List[SearchExchangeListItemOutputModel] = exchange_service.search(
        search_exchange_input_dto.to_model()
    )

    return [
        SearchExchangeListItemOutputDto(**exchange_item.dict())
        for exchange_item in search_result
    ]
