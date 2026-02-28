from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: mapped_column(Integer, primary_key=True)
    wb_id: mapped_column(Integer, unique=True)
    name: mapped_column(String)
    price: mapped_column(Float)
    price_old: mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
