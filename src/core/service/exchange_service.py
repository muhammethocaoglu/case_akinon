from typing import List

from src.core.model.create_exchange_input_model import CreateExchangeInputModel
from src.core.model.create_exchange_output_model import (
    CreateExchangeOutputModel,
    ExchangeCalculationResultModel,
)
from src.core.model.create_exchange_transaction_input_model import (
    CreateExchangeTransactionInputModel,
)
from src.core.model.create_exchange_transaction_output_model import (
    CreateExchangeTransactionOutputModel,
)
from src.core.model.retrieve_exchange_rates_input_model import (
    RetrieveExchangeRatesInputModel,
)
from src.core.model.retrieve_exchange_rates_output_model import (
    RetrieveExchangeRateOutputModel,
)
from src.core.model.search_exchange_input_model import SearchExchangeInputModel
from src.core.model.search_exchange_list_item_output_model import (
    SearchExchangeListItemOutputModel,
)
from src.core.port.exchange_port import ExchangePort
from src.core.port.exchange_rate_port import ExchangeRatePort
from src.infra.exception.bad_request_exception import BadRequestException


class ExchangeService:
    def __init__(
        self, exchange_port: ExchangePort, exchange_rate_port: ExchangeRatePort
    ):
        self.exchange_port = exchange_port
        self.exchange_rate_port = exchange_rate_port

    def create(
        self, create_exchange_input_model: CreateExchangeInputModel
    ) -> CreateExchangeOutputModel:
        retrieve_exchange_rate_output_model_list: List[
            RetrieveExchangeRateOutputModel
        ] = self.exchange_rate_port.retrieve_rates(
            RetrieveExchangeRatesInputModel(**create_exchange_input_model.dict())
        )
        target_amounts, target_currencies = self._populate_target_currencies_amounts(
            create_exchange_input_model, retrieve_exchange_rate_output_model_list
        )

        create_exchange_transaction_output_model: CreateExchangeTransactionOutputModel = self.exchange_port.create(
            CreateExchangeTransactionInputModel(
                source_amount=create_exchange_input_model.source_amount,
                source_currency=create_exchange_input_model.source_currency,
                target_currencies=target_currencies,
                target_amounts=target_amounts,
            )
        )

        return CreateExchangeOutputModel(
            id=create_exchange_transaction_output_model.id,
            exchange_results=[
                ExchangeCalculationResultModel(
                    target_currency=target_currency,
                    target_amount=target_amounts[index],
                )
                for index, target_currency in enumerate(target_currencies)
            ],
        )

    def search(
        self, search_exchange_input_model: SearchExchangeInputModel
    ) -> List[SearchExchangeListItemOutputModel]:
        self._validate_search_exchange_input_model(search_exchange_input_model)
        return self.exchange_port.search(search_exchange_input_model)

    @staticmethod
    def _validate_search_exchange_input_model(search_exchange_input_model):
        if search_exchange_input_model.id is not None:
            if search_exchange_input_model.start_date is not None or search_exchange_input_model.end_date is not None:
                raise BadRequestException(error_code=2001)
        else:
            if search_exchange_input_model.start_date is None and search_exchange_input_model.end_date is None:
                raise BadRequestException(error_code=2001)

    @staticmethod
    def _populate_target_currencies_amounts(
        create_exchange_input_model, retrieve_exchange_rate_output_model_list
    ):
        target_currencies = []
        target_amounts = []
        for exchange_rate_output in retrieve_exchange_rate_output_model_list:
            target_currencies.append(exchange_rate_output.target_currency)
            target_amounts.append(
                exchange_rate_output.rate * create_exchange_input_model.source_amount
            )
        return target_amounts, target_currencies
