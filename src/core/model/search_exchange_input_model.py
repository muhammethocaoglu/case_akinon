from datetime import date
from typing import Optional

from pydantic import BaseModel


class SearchExchangeInputModel(BaseModel):
    id: Optional[int]
    start_date: Optional[date]
    end_date: Optional[date]
