from pydantic import BaseModel


class ExchangeRateOutputDto(BaseModel):
    target_currency: str
    rate: float
