from typing import cast

from src.core.port.exchange_port import ExchangePort
from src.core.port.exchange_rate_port import ExchangeRatePort
from src.infra.adapter.client.exchange_rate_fake_client_adapter import ExchangeRateFakeClientAdapter
from src.infra.adapter.client.exchange_rate_fixerio_client_adapter import (
    ExchangeRateFixerIoClientAdapter,
)
from src.infra.adapter.repository.postgres.exchange_postgres_repository_adapter import (
    ExchangePostgresRepositoryAdapter,
)
from src.infra.config.app_config import TEST_MODE


def get_exchange_rate_adapter():
    if TEST_MODE:
        return cast(ExchangeRatePort, ExchangeRateFakeClientAdapter())
    return cast(ExchangeRatePort, ExchangeRateFixerIoClientAdapter())


def get_exchange_adapter():
    return cast(ExchangePort, ExchangePostgresRepositoryAdapter())
