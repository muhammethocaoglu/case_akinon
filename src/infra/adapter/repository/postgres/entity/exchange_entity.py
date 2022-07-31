from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.dialects.postgresql import ARRAY

from src.infra.adapter.repository.postgres.repository_config import Base


class ExchangeEntity(Base):
    __tablename__ = "exchanges"
    id = Column(Integer, primary_key=True)
    created_at = Column(Date, default=datetime.utcnow().date(), nullable=False)
    source_amount = Column(Float, nullable=False)
    source_currency = Column(String, nullable=False)
    target_currencies = Column(ARRAY(String), nullable=False)
    target_amounts = Column(ARRAY(Float), nullable=False)
