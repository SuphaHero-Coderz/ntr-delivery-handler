from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class Driver(SQLModel, table=True):
    __tablename__: str = "drivers"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Delivery(SQLModel, table=True):
    __tablename__: str = "payments"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    order_id: int
    start_timestamp: Optional[datetime] = Field(default=datetime.utcnow())
    delivered_timestamp: Optional[datetime] = Field(default=None)
