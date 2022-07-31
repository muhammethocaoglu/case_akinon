from typing import List

from src.core.model.retrieve_exchange_rates_input_model import (
    RetrieveExchangeRatesInputModel,
)
from src.core.model.retrieve_exchange_rates_output_model import (
    RetrieveExchangeRateOutputModel,
)
from src.core.port.exchange_rate_port import ExchangeRatePort


class ExchangeRateService:
    def __init__(self, exchange_rate_port: ExchangeRatePort):
        self.exchange_rate_port = exchange_rate_port

    def retrieve_exchange_rates(
        self,
        retrieve_exchange_rates_input_model: RetrieveExchangeRatesInputModel,
    ) -> List[RetrieveExchangeRateOutputModel]:
        return self.exchange_rate_port.retrieve_rates(
            retrieve_exchange_rates_input_model
        )
