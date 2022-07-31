from pytest import raises

from src.core.model.retrieve_exchange_rates_input_model import (
    RetrieveExchangeRatesInputModel,
)
from src.infra.exception.infra_exception import InfraException


class TestExchangeRateService:
    def test_should_raise_error_when_retrieve_exchange_rates_if_exchange_client_raises_infra_exception(
        self, exchange_rate_service
    ):
        # given
        retrieve_exchange_rates_input_model: RetrieveExchangeRatesInputModel = (
            RetrieveExchangeRatesInputModel(
                source_currency="Unknown", target_currency_list=["GBP", "EUR"]
            )
        )
        # when
        with raises(InfraException) as infra_exc:
            exchange_rate_service.retrieve_exchange_rates(
                retrieve_exchange_rates_input_model
            )
        # then
        assert infra_exc.value.error_code == 2000
