from src.infra.adapter.repository.postgres.entity.exchange_entity import ExchangeEntity
from src.infra.adapter.repository.postgres.repository_manager import RepositoryManager


def delete_exchange_table():
    with RepositoryManager() as repository_manager:
        repository_manager.query(ExchangeEntity).delete()
        repository_manager.commit()
