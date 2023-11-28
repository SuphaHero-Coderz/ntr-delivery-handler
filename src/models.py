from sqlmodel import Field, SQLModel, Relationship
from typing import Optional

class Driver(SQLModel, table=True):
    __tablename__: str = "drivers"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    deliveries: Optional["Delivery"] = Relationship(back_populates="driver")


class Delivery(SQLModel, table=True):
    __tablename__: str = "deliveries"

    id: Optional[int] = Field(default=None, primary_key=True)
    driver_id: Optional[int] = Field(default=None, foreign_key="drivers.id")
    driver: Optional[Driver] = Relationship(back_populates="deliveries")
    user_id: int
    order_id: int
    delivered: Optional[bool] = Field(default=False)
