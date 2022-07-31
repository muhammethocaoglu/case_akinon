from typing import List

import pytest

from src.core.model.create_exchange_transaction_input_model import (
    CreateExchangeTransactionInputModel,
)
from src.core.model.create_exchange_transaction_output_model import (
    CreateExchangeTransactionOutputModel,
)
from src.core.model.search_exchange_input_model import SearchExchangeInputModel
from src.core.model.search_exchange_list_item_output_model import (
    SearchExchangeListItemOutputModel,
    ExchangeResultModel,
)
from tests.test_input_common import (
    delete_exchange_table,
)


@pytest.fixture(autouse=True)
def clear_all_tables_before_after_each_method():
    delete_exchange_table()
    yield
    delete_exchange_table()


class TestExchangeRepositoryPostgresAdapter:
    def test_should_create_and_search(
        self,
        exchange_postgres_repository_adapter,
    ):
        # given
        create_exchange_input_model: CreateExchangeTransactionInputModel = (
            CreateExchangeTransactionInputModel(
                source_amount=50,
                source_currency="GBP",
                target_amounts=[60, 70],
                target_currencies=["TRY", "USD"],
            )
        )
        # when
        create_exchange_output_model: CreateExchangeTransactionOutputModel = (
            exchange_postgres_repository_adapter.create(create_exchange_input_model)
        )
        # then
        retrieved_exchanges: List[
            SearchExchangeListItemOutputModel
        ] = exchange_postgres_repository_adapter.search(
            SearchExchangeInputModel(id=create_exchange_output_model.id)
        )
        assert len(retrieved_exchanges) == 1
        actual_exchange = retrieved_exchanges[0]
        assert (
            actual_exchange.source_currency
            == create_exchange_input_model.source_currency
        )
        assert (
            actual_exchange.source_amount == create_exchange_input_model.source_amount
        )
        assert actual_exchange.exchange_results == [
            ExchangeResultModel(
                target_currency=create_exchange_input_model.target_currencies[index],
                target_amount=amount,
            )
            for index, amount in enumerate(create_exchange_input_model.target_amounts)
        ]
