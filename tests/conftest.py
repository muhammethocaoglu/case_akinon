import pytest
from starlette.testclient import TestClient

from main import app
from src.core.service.exchange_rate_service import ExchangeRateService
from src.core.service.exchange_service import ExchangeService
from src.infra.adapter.client.exchange_rate_fake_client_adapter import (
    ExchangeRateFakeClientAdapter,
)
from src.infra.adapter.repository.postgres.exchange_postgres_repository_adapter import (
    ExchangePostgresRepositoryAdapter,
)


@pytest.fixture(scope="session")
def test_client():
    return TestClient(app, base_url="http://localhost")


@pytest.fixture(scope="session")
def exchange_postgres_repository_adapter():
    return ExchangePostgresRepositoryAdapter()


@pytest.fixture(scope="session")
def exchange_rate_adapter():
    return ExchangeRateFakeClientAdapter()


@pytest.fixture(scope="session")
def exchange_rate_service(exchange_rate_adapter):
    return ExchangeRateService(exchange_rate_adapter)


@pytest.fixture(scope="session")
def exchange_service(exchange_rate_adapter, exchange_postgres_repository_adapter):
    return ExchangeService(
        exchange_port=exchange_postgres_repository_adapter, exchange_rate_port=exchange_rate_adapter
    )
