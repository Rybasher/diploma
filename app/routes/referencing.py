from typing import List

from fastapi import APIRouter, Depends, status, UploadFile, File
from pydantic import BaseModel

from app.crud.text_base import CRUDText
from app.dependencies.crud_dependency import get_text_crud_dependency, get_tex_info_crud_dependency
from app.schemas.referencing import TextModel, TextInfoResponse, TextCreateResponse, ReferencingResponse
from app.services.referencing import Referencing
from app.database.session import get_db
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.utils.exceptions import TextNotFound
from app.utils.utils import row2dict

router = APIRouter(tags=["referencing"])


@router.post("/referencing/text-info/{text_id}", response_model=TextInfoResponse, status_code=201)
async def get_text_info(text_id: str, crud_text: CRUDText = Depends(get_text_crud_dependency),
                        crud_info: CRUDText = Depends(get_tex_info_crud_dependency),
                        db: Session = Depends(get_db)) -> JSONResponse:
    try:
        text = await crud_text.get(db=db, id=text_id)
    except TextNotFound as error:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
            "message": error.detail
        })

    reference_instance = Referencing(text)
    result = await reference_instance.get_text_info()
    await crud_info.add_info_to_text_instance(db=db, obj_in=result, text_id=int(text_id))
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "symbols": result.symbols,
        "symbols_without_whitespaces": result.symbols_w_w,
        "words_count": result.words_count,
        "sentences_count": result.sentences_count,
        "hot_word": result.hot_word,
        "hot_word_count": int(result.hot_word_count)
    })


@router.post("/referencing/add_text/", response_model=TextCreateResponse)
async def add_text(text_example: TextModel, crud: CRUDText = Depends(get_text_crud_dependency),
                   db: Session = Depends(get_db)) -> JSONResponse:
    result = await crud.create(db=db, obj_in=text_example)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"id": result.id, "text": result.your_text})


@router.post("/referencing/add_text/file/", response_model=TextCreateResponse)
async def add_text_from_file(file: UploadFile = File(...), crud: CRUDText = Depends(get_text_crud_dependency),
                             db: Session = Depends(get_db)):
    content = await file.read()
    result = await crud.create(db=db, obj_in=TextModel(your_text=content.decode("utf-8").rstrip("\n")))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"id": result.id, "text": result.your_text})


@router.get("/referencing/get_text/{text_id}", response_model=TextCreateResponse)
async def get_text_by_id(text_id: str, crud: CRUDText = Depends(get_text_crud_dependency),
                         db: Session = Depends(get_db)) -> JSONResponse:
    result = await crud.get(db=db, id=text_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"id": result.id, "text": result.your_text})


@router.get("/referencing/get_referencing_result/{text_id}", response_model=ReferencingResponse)
async def get_referencing_result(text_id: str, crud: CRUDText = Depends(get_text_crud_dependency),
                                 crud_info: CRUDText = Depends(get_tex_info_crud_dependency),
                                 db: Session = Depends(get_db)) -> JSONResponse:
    text = await crud.get(db=db, id=text_id)
    ref_instance = Referencing(text)
    result = await ref_instance.referencing_text()
    await crud_info.add_info_to_text_instance(db=db, obj_in=result, text_id=int(text_id))
    return JSONResponse(status_code=status.HTTP_200_OK, content=result.dict())


@router.get("/referencing/list_of_referencing", response_model=List[ReferencingResponse])
async def get_list_of_referencing(skip: int = 0, limit: int = 10,
                                  crud_info: CRUDText = Depends(get_tex_info_crud_dependency),
                                  db: Session = Depends(get_db)) -> List[BaseModel]:
    return await row2dict(ReferencingResponse, await crud_info.get_multi(db, skip=skip, limit=limit))
