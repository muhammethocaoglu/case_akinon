from pydantic import BaseModel


class RetrieveExchangeRateOutputModel(BaseModel):
    target_currency: str
    rate: float
