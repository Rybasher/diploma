import sqlalchemy
from app.core import config
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine(
    config.DB_DEFAULT
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
