from typing import List

from pydantic import BaseModel, Field


class CreateExchangeInputDto(BaseModel):
    source_amount: float = Field(..., example=10)
    source_currency: str = Field(default="EUR", example="EUR")
    target_currency_list: List[str] = Field(..., example=["USD", "GBP"])
