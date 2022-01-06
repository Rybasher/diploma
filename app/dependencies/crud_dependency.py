from app.crud.text_base import CRUDText
from app.database.models.text import Text, TextInfo


def get_text_crud_dependency():
    return CRUDText(Text)


def get_tex_info_crud_dependency():
    return CRUDText(TextInfo)

