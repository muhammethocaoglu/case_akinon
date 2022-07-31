from typing import List

from src.core.model.retrieve_exchange_rates_input_model import (
    RetrieveExchangeRatesInputModel,
)
from src.core.model.retrieve_exchange_rates_output_model import (
    RetrieveExchangeRateOutputModel,
)
from src.infra.exception.infra_exception import InfraException


class ExchangeRateFakeClientAdapter:
    def retrieve_rates(
        self, retrieve_exchange_rates_input_model: RetrieveExchangeRatesInputModel
    ) -> List[RetrieveExchangeRateOutputModel]:
        if retrieve_exchange_rates_input_model.source_currency == "Unknown":
            raise InfraException(error_code=2000)
        return [
            RetrieveExchangeRateOutputModel(target_currency="USD", rate=1.01),
            RetrieveExchangeRateOutputModel(target_currency="GBP", rate=0.92),
        ]
