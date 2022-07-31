from typing import Protocol, List

from src.core.model.create_exchange_transaction_input_model import (
    CreateExchangeTransactionInputModel,
)
from src.core.model.create_exchange_transaction_output_model import (
    CreateExchangeTransactionOutputModel,
)
from src.core.model.search_exchange_input_model import SearchExchangeInputModel
from src.core.model.search_exchange_list_item_output_model import SearchExchangeListItemOutputModel


class ExchangePort(Protocol):
    @staticmethod
    def create(
        create_exchange_transaction_input_model: CreateExchangeTransactionInputModel,
    ) -> CreateExchangeTransactionOutputModel:
        ...

    @staticmethod
    def search(search_exchange_input_model: SearchExchangeInputModel) -> List[SearchExchangeListItemOutputModel]:
        ...
