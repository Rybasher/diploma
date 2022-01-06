from app.crud.base import CRUDBase
from app.database.models.text import Text
from app.schemas.referencing import TextModel


class CRUDText(CRUDBase[Text, TextModel]):
    pass


