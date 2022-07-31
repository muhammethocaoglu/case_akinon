from typing import List

from pydantic import BaseModel


class ExchangeCalculationResultModel(BaseModel):
    target_currency: str
    target_amount: float


class CreateExchangeOutputModel(BaseModel):
    id: int
    exchange_results: List[ExchangeCalculationResultModel]
