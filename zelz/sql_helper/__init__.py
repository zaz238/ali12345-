import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


def start() -> scoped_session:
    database_url = (
        Config.DB_URI.replace("postgres:", "postgresql:")
        if "postgres://" in Config.DB_URI
        else Config.DB_URI
    )
    engine = create_engine(database_url)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    LOGS.error(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    LOGS.error(str(e))
