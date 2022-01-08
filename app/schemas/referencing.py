from typing import Dict

from pydantic import BaseModel


class TextModel(BaseModel):
    your_text: str


class TextCreateResponse(BaseModel):
    id: int
    text: str


class TextInfoResponse(BaseModel):
    symbols: int
    symbols_w_w: int
    words_count: int
    sentences_count: int
    hot_word: str
    hot_word_count: int


class ReferencingResponse(TextInfoResponse):
    hot_words: Dict[str, int]
    text_water: str
    new_text: str


