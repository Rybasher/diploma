from typing import List, Union, Text
from pydantic import BaseModel


async def row2dict(model: BaseModel, db_row: List[Union[Text, Text]]) -> List[BaseModel]:
    return [model.parse_obj(column.__dict__) for column in db_row]
