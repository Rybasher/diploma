from pydantic import BaseModel


class NlpEntitiesResponse(BaseModel):
    text: str
    ent_proc: str


class UpdatePattern(BaseModel):
    label: str
    pattern: str
