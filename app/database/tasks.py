from fastapi import FastAPI
from databases import Database
from app.core.config import DATABASE_URL
import logging
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


async def connect_to_db(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2, max_size=10)

    try:
        await database.connect()
        app.state._db = database
        logging.info("-------- DATABASE CONNECTION SUCCESS")
    except Exception as e:
        logger.warning(DATABASE_URL)
        logger.warning("-------- DATABASE CONNECTION ERROR")
        logger.warning(e)
        logger.warning("-------- DATABASE CONNECTION ERROR")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
        logging.info("-------- DATABASE DISCONNECT SUCCESS")

    except Exception as e:
        logger.warning("-------- DATABASE DISCONNECT ERROR")
        logger.warning(e)
        logger.warning("-------- DATABASE DISCONNECT ERROR")



