import src.database as _database
import random

from src.models import Driver, Delivery
from src.database import engine
from sqlmodel import Session, select
from typing import List


"""
DATABASE ZONE
"""


def create_database() -> None:
    """
    Initializes the database engine
    """
    _database.init_db()


"""
DRIVER ZONE
"""


def populate_drivers() -> None:
    """
    Populates the drivers table with drivers
    """
    with Session(engine) as session:
        drivers = [
            Driver(name="Ryan Gosling"),
            Driver(name="Dominic Toretto"),
            Driver(name="Baby Driver"),
        ]

        for driver in drivers:
            session.add(driver)

        session.commit()


def get_random_driver() -> Driver:
    with Session(engine) as session:
        query = select(Driver)
        drivers: List[Driver] = session.exec(query).all()

        return random.choice(drivers)


"""
DELIVERY ZONE
"""


def create_delivery(delivery: Delivery) -> Delivery:
    with Session(engine) as session:
        session.add(delivery)
        session.commit()
        session.refresh(delivery)
        return delivery


def mark_delivery_as_complete(delivery_id: int) -> None:
    with Session(engine) as session:
        query = select(Delivery).where(Delivery.id == delivery_id)
        delivery: Delivery = session.exec(query).one()
        delivery.delivered = True
        session.add(delivery)
        session.commit()
