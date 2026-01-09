from sqlalchemy import Column, Integer, String
from db.database import Base

class Asset(Base):
    __tablename__ = "assets"

    asset_id = Column(Integer, primary_key=True)
    asset_type = Column(String, nullable=False)      # cash, crypto, equity
    symbol = Column(String, nullable=False)          # BTC, EUR, VWCE
    name = Column(String, nullable=True)
    source = Column(String, nullable=False)          # coinbase, manual
    native_currency = Column(String, nullable=False) # EUR, USD
