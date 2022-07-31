from typing import Protocol, List

from src.core.model.retrieve_exchange_rates_input_model import RetrieveExchangeRatesInputModel
from src.core.model.retrieve_exchange_rates_output_model import RetrieveExchangeRateOutputModel


class ExchangeRatePort(Protocol):

    def retrieve_rates(self, retrieve_exchange_rates_input_model: RetrieveExchangeRatesInputModel) -> List[RetrieveExchangeRateOutputModel]:
        ...
