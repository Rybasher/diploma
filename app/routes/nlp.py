from fastapi import APIRouter, Depends, status

from app.crud.text_base import CRUDText
from app.dependencies.crud_dependency import get_text_crud_dependency
from app.dependencies.nlp import get_sm_nlp_model, get_md_nlp_model
from app.schemas.nlp import UpdatePattern
from app.services.nlp import SmNlpModel
from app.database.session import get_db
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.utils.exceptions import TextNotFound

router = APIRouter(tags=["nlp"])


@router.get("/nlp/sm/get_entities/{text_id}")
async def get_entities(text_id: str, sm_nlp_model: SmNlpModel = Depends(get_sm_nlp_model),
                       crud_text: CRUDText = Depends(get_text_crud_dependency),
                       db: Session = Depends(get_db)) -> JSONResponse:
    try:
        text = (await crud_text.get(db=db, id=text_id)).your_text
    except TextNotFound as error:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
            "message": error.detail
        })
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=(await sm_nlp_model.get_text_with_entities(text)).dict())


@router.get("/nlp/sm/add_pattern/{text_id}")
async def get_entities_with_new_pattern(text_id: str, pattern: UpdatePattern = Depends(),
                                        sm_nlp_model: SmNlpModel = Depends(get_md_nlp_model),
                                        crud_text: CRUDText = Depends(get_text_crud_dependency),
                                        db: Session = Depends(get_db)) -> JSONResponse:
    try:
        text = (await crud_text.get(db=db, id=text_id)).your_text
    except TextNotFound as error:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
            "message": error.detail
        })
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=(await sm_nlp_model.get_text_entities_with_updated_pattern(text, pattern)).dict())


@router.get("/nlp/sm/get_facts/{text_id}")
async def get_facts(text_id: str, word: str, sm_nlp_model: SmNlpModel = Depends(get_md_nlp_model),
                    crud_text: CRUDText = Depends(get_text_crud_dependency),
                    db: Session = Depends(get_db)) -> JSONResponse:
    try:
        text = (await crud_text.get(db=db, id=text_id)).your_text
    except TextNotFound as error:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
            "message": error.detail
        })
    result = await sm_nlp_model.get_fact(text, word)
    return JSONResponse(status_code=status.HTTP_200_OK, content={})

