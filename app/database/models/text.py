import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship
from app.database.db import Base


class Text(Base):
    id = Column(Integer, primary_key=True, index=True)
    your_text = Column(Text, nullable=False)
    info = relationship("TextInfo", back_populates="text")


class TextInfo(Base):

    id = Column(Integer, primary_key=True, index=True)
    symbols = Column(Integer)
    symbols_w_w = Column(Integer)
    words_count = Column(Integer)
    sentences_count = Column(Integer)
    hot_word = Column(String)
    hot_word_count = Column(Integer)
    hot_words = Column(JSON)
    text_water = Column(String)
    new_text = Column(sqlalchemy.Text)
    text_id = Column(Integer, ForeignKey("text.id"))
    text = relationship("Text",  back_populates="info")
