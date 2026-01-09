from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from db.database import Base

class Balance(Base):
    __tablename__ = "balances"

    balance_id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey("assets.asset_id"), nullable=False)
    quantity = Column(Float, nullable=False)
    as_of_date = Column(Date, nullable=False)
