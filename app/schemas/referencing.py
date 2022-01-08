from typing import Dict, Optional

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
    hot_words: Optional[Dict[str, int]] = None
    text_water: Optional[str] = None
    new_text: Optional[str] = None


