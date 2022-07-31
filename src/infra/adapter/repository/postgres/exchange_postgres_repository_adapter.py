from typing import List

from sqlalchemy import and_

from src.core.model.create_exchange_transaction_input_model import (
    CreateExchangeTransactionInputModel,
)
from src.core.model.create_exchange_transaction_output_model import (
    CreateExchangeTransactionOutputModel,
)
from src.core.model.search_exchange_input_model import SearchExchangeInputModel
from src.core.model.search_exchange_list_item_output_model import (
    SearchExchangeListItemOutputModel,
    ExchangeResultModel,
)
from src.infra.adapter.repository.postgres.entity.exchange_entity import ExchangeEntity
from src.infra.adapter.repository.postgres.repository_manager import RepositoryManager


class ExchangePostgresRepositoryAdapter:
    @staticmethod
    def create(
        create_exchange_input_model: CreateExchangeTransactionInputModel,
    ) -> CreateExchangeTransactionOutputModel:
        with RepositoryManager() as repository_manager:
            exchange_entity = ExchangeEntity(**create_exchange_input_model.dict())
            repository_manager.add(exchange_entity)
            repository_manager.commit()
            return CreateExchangeTransactionOutputModel(id=exchange_entity.id)

    @staticmethod
    def search(
        search_exchange_input_model: SearchExchangeInputModel,
    ) -> List[SearchExchangeListItemOutputModel]:
        with RepositoryManager() as repository_manager:
            retrieved_exchange_items: List[SearchExchangeListItemOutputModel] = []
            if search_exchange_input_model.id is not None:
                retrieved_exchange_entity: ExchangeEntity = (
                    repository_manager.query(ExchangeEntity)
                    .filter(ExchangeEntity.id == search_exchange_input_model.id)
                    .first()
                )
                if retrieved_exchange_entity is not None:
                    retrieved_exchange_items.append(
                        ExchangePostgresRepositoryAdapter._populate_search_exchange_list_item_output_model(
                            retrieved_exchange_entity
                        )
                    )
            else:
                list_exchanges_result = repository_manager.query(ExchangeEntity).filter(
                    and_(
                        ExchangeEntity.created_at
                        <= search_exchange_input_model.end_date,
                        ExchangeEntity.created_at
                        >= search_exchange_input_model.start_date,
                    )
                )
                for exchange in list_exchanges_result:
                    retrieved_exchange_items.append(
                        ExchangePostgresRepositoryAdapter._populate_search_exchange_list_item_output_model(
                            exchange
                        )
                    )
            return retrieved_exchange_items

    @staticmethod
    def _populate_search_exchange_list_item_output_model(retrieved_exchange_entity):
        return SearchExchangeListItemOutputModel(
            id=retrieved_exchange_entity.id,
            source_currency=retrieved_exchange_entity.source_currency,
            source_amount=retrieved_exchange_entity.source_amount,
            exchange_date=retrieved_exchange_entity.created_at,
            exchange_results=[
                ExchangeResultModel(
                    target_currency=target_currency,
                    target_amount=retrieved_exchange_entity.target_amounts[index],
                )
                for index, target_currency in enumerate(retrieved_exchange_entity.target_currencies)
            ],
        )
