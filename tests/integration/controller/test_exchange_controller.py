from datetime import datetime, timedelta

import pytest
from starlette import status

from src.api.controller.dto.create_exchange_input_dto import CreateExchangeInputDto
from src.api.controller.dto.search_exchange_list_item_output_dto import (
    SearchExchangeListItemOutputDto,
    ExchangeResultDto,
)
from tests.test_input_common import (
    delete_exchange_table,
)


@pytest.fixture(autouse=True)
def clear_exchange_table_before_after_each_method():
    delete_exchange_table()
    yield
    delete_exchange_table()


class TestExchangeController:
    def test_should_create_and_search_exchanges(
        self, test_client, exchange_rate_adapter
    ):
        # given
        create_exchange_input_dto: CreateExchangeInputDto = CreateExchangeInputDto(
            source_amount=100,
            source_currency="TRY",
            target_currency_list=["USD", "GBP"],
        )
        retrieve_exchange_rates_response = test_client.get(
            "api/v1/exchange-rates",
            params={
                "source_currency": create_exchange_input_dto.source_currency,
                "target_currency_list": create_exchange_input_dto.target_currency_list,
            },
        )
        # when
        create_response = test_client.post(
            "/api/v1/exchanges",
            data=create_exchange_input_dto.json(),
        )

        # then
        response = test_client.get(
            "/api/v1/exchanges",
            params={
                "start_date": (datetime.utcnow() - timedelta(days=4)).date(),
                "end_date": (datetime.utcnow() + timedelta(days=4)).date(),
            },
        )

        # then
        assert response.status_code == status.HTTP_200_OK
        retrieved_exchanges = [
            SearchExchangeListItemOutputDto(**item) for item in response.json()
        ]
        assert len(retrieved_exchanges) == 1
        exchange = retrieved_exchanges[0]
        assert exchange.source_currency == create_exchange_input_dto.source_currency
        assert exchange.source_amount == create_exchange_input_dto.source_amount
        assert exchange.exchange_results == [
            ExchangeResultDto(
                target_currency=item["target_currency"],
                target_amount=create_exchange_input_dto.source_amount * item["rate"],
            )
            for item in retrieve_exchange_rates_response.json()
        ]
