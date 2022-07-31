from starlette import status

from src.api.controller.dto.exchange_rate_output_dto import ExchangeRateOutputDto


class TestExchangeRateController:
    def test_should_retrieve_exchange_rates(self, test_client):
        # given
        # when
        retrieve_exchange_rates_response = test_client.get(
            "api/v1/exchange-rates",
            params={"source_currency": "JPY", "target_currency_list": ["USD", "GBP"]},
        )

        # then
        assert retrieve_exchange_rates_response.status_code == status.HTTP_200_OK
        assert retrieve_exchange_rates_response.json() == [
            ExchangeRateOutputDto(target_currency="USD", rate=1.01).dict(),
            ExchangeRateOutputDto(target_currency="GBP", rate=0.92).dict(),
        ]
