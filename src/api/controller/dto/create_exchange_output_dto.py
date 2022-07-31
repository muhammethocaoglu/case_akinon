from typing import List

from pydantic import BaseModel, Field


class ExchangeCalculationResultDto(BaseModel):
    target_currency: str = Field(..., example="USD")
    target_amount: float = Field(..., example=10)


class CreateExchangeOutputDto(BaseModel):
    id: int = Field(..., example=1)
    exchange_results: List[ExchangeCalculationResultDto]
