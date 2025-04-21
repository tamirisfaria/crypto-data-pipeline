from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'

    id = Column(String, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    rank = Column(Integer)
    prices = relationship("Price", back_populates="crypto")

class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    crypto_id = Column(String, ForeignKey('cryptocurrencies.id'))
    price_usd = Column(Float)
    market_cap = Column(Float)
    volume_24h = Column(Float)
    timestamp = Column(DateTime)

    crypto = relationship("Cryptocurrency", back_populates="prices")
