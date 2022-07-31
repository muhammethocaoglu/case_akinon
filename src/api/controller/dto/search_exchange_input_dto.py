from datetime import date, datetime
from typing import Optional

from fastapi import Query

from src.core.model.search_exchange_input_model import SearchExchangeInputModel


class SearchExchangeInputDto:
    def __init__(
        self,
        id: Optional[int] = Query(default=None, example=1, ge=1),
        start_date: date = Query(default=None, example=datetime.utcnow().date()),
        end_date: date = Query(default=None, example=datetime.utcnow().date()),
    ):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date

    def to_model(self) -> SearchExchangeInputModel:
        return SearchExchangeInputModel(
            id=self.id, start_date=self.start_date, end_date=self.end_date
        )
