from sqlalchemy import Column, Integer, Float, String, Date
from db.database import Base

class Price(Base):
    __tablename__ = "prices"

    price_id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    price_date = Column(Date, nullable=False)
    source = Column(String, nullable=False)
