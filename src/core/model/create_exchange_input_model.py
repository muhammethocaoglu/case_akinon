from typing import List

from pydantic import BaseModel


class CreateExchangeInputModel(BaseModel):
    source_amount: float
    source_currency: str
    target_currency_list: List[str]
