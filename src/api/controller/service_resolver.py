from src.core.service.exchange_rate_service import ExchangeRateService
from src.core.service.exchange_service import ExchangeService
from src.infra.config.dependency_injection_config import (
    get_exchange_rate_adapter,
    get_exchange_adapter,
)


def get_exchange_rate_service():
    return ExchangeRateService(get_exchange_rate_adapter())


def get_exchange_service():
    return ExchangeService(
        exchange_port=get_exchange_adapter(),
        exchange_rate_port=get_exchange_rate_adapter(),
    )
