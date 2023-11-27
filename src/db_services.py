import src.database as _database

from src.models import Driver, Delivery
from src.database import engine
from sqlmodel import Session


"""
DATABASE ZONE
"""


def create_database() -> None:
    """
    Initializes the database engine
    """
    _database.init_db()


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


"""
DELIVERY ZONE
"""


def create_delivery(delivery: Delivery):
    with Session(engine) as session:
        session.add(delivery)
        session.commit()
