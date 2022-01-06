from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database.db import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(Text, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False, unique=True)
