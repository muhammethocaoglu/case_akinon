from typing import List

import requests
from starlette import status

from src.core.model.retrieve_exchange_rates_input_model import (
    RetrieveExchangeRatesInputModel,
)
from src.core.model.retrieve_exchange_rates_output_model import (
    RetrieveExchangeRateOutputModel,
)
from src.infra.config.app_config import (
    FIXER_IO_BASE_URL,
    FIXER_IO_LATEST_ENDPOINT_CONTEXT_PATH,
    FIXER_IO_API_KEY,
)
from src.infra.exception.infra_exception import InfraException


class ExchangeRateFixerIoClientAdapter:
    def __init__(self):
        self.request_url = FIXER_IO_BASE_URL + FIXER_IO_LATEST_ENDPOINT_CONTEXT_PATH
        self.api_key_header = {"apikey": FIXER_IO_API_KEY}

    def retrieve_rates(
        self, retrieve_exchange_rates_input_model: RetrieveExchangeRatesInputModel
    ) -> List[RetrieveExchangeRateOutputModel]:
        try:
            response = requests.get(
                url=self.request_url,
                headers=self.api_key_header,
                params={
                    "base": retrieve_exchange_rates_input_model.source_currency,
                    "symbols": ",".join(
                        retrieve_exchange_rates_input_model.target_currency_list
                    ),
                },
            )
            response_data = response.json()
            if response.status_code != status.HTTP_200_OK:
                raise InfraException(
                    error_code=2000,
                    error_detail=f"Fixer io returns {response_data}"
                    if response_data is not None
                    else None,
                )
            return [
                RetrieveExchangeRateOutputModel(
                    target_currency=target_currency, rate=rate
                )
                for target_currency, rate in response_data["rates"].items()
            ]

        except InfraException as infra_exc:
            raise infra_exc
        except Exception as exc:
            raise InfraException(error_code=1999) from exc
