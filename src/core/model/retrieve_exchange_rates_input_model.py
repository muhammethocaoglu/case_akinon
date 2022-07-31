from typing import List

from pydantic import BaseModel


class RetrieveExchangeRatesInputModel(BaseModel):
    source_currency: str
    target_currency_list: List[str]
