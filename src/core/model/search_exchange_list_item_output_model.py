from datetime import date
from typing import List

from pydantic import BaseModel


class ExchangeResultModel(BaseModel):
    target_currency: str
    target_amount: float


class SearchExchangeListItemOutputModel(BaseModel):
    id: int
    source_currency: str
    source_amount: float
    exchange_date: date
    exchange_results: List[ExchangeResultModel]
