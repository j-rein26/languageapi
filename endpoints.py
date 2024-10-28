from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
import models
import schemas


router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/functions/", response_model=List[schemas.FunctionOut])
def create_function(function: schemas.FunctionCreate, db: Session=Depends(get_db)):
    #db_function = models.Functions(**function.model_dump())
    db_function = models.Functions(
    english=function.english,
    turkish=function.turkish,
    examples=function.examples  # This can contain newline-separated examples
)

    db.add(db_function)
    db.commit()
    db.refresh(db_function)
    return db_function

@router.get("/functions/", response_model=List[schemas.FunctionOut])
def read_functions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    functions = db.query(models.Functions).offset(skip).limit(limit).all()
    return functions

@router.get("/functions/{function_id}", response_model=List[schemas.FunctionOut])
def read_function(function_id: int, db: Session = Depends(get_db)):
    function = db.query(models.Functions).filter(models.Functions.id == function_id).first()
    if function is None:
        raise HTTPException(status_code=404, detail="Function not found")
    
    # Ensure examples is a string
    if isinstance(function.examples, list):
        function.examples = '\n'.join(function.examples)

    return function

@router.put("/functions/{function_id}", response_model=List[schemas.FunctionOut])
def update_function(function_id: int, function: schemas.FunctionCreate, db: Session = Depends(get_db)):
    db_function = db.query(models.Functions).filter(models.Functions.id == function_id).first()
    if db_function is None:
        raise HTTPException(status_code=404, detail="Function not found")
    
    for key, value in function.model_dump().items():
        setattr(db_function, key, value)
    db.commit()
    db.refresh(db_function)
    return db_function

@router.delete("/functions/{function_id}", response_model=List[schemas.FunctionOut])
def delete_function(function_id: int, db: Session = Depends(get_db)):
    db_function = db.query(models.Functions).filter(models.Functions.id == function_id).first()
    if db_function is None:
        raise HTTPException(status_code=404, detail="Function not found")
    
    db.delete(db_function)
    db.commit()
    return db_function