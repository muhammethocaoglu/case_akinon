from typing import List

from pydantic import BaseModel


class CreateExchangeTransactionInputModel(BaseModel):
    source_amount: float
    source_currency: str
    target_amounts: List[float]
    target_currencies: List[str]
