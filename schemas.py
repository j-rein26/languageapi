from pydantic import BaseModel



class FunctionCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to FunctionCreate
        orm_mode = True

class FunctionOut(FunctionCreate):
    id: int

    class Config:
        # Configuration options specific to FunctionOut
        orm_mode = True

class SequenceCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to SequenceCreate
        orm_mode = True

class SequenceOut(SequenceCreate):
    id: int

    class Config:
        # Configuration options specific to SequenceOut
        orm_mode = True

class RelataedActionCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to RelatedActionCreate
        orm_mode = True

class RelatedActionOut(RelataedActionCreate):
    id: int

    class Config:
        # Configuration options specific to RelatedActionOut
        orm_mode = True

class OperationCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to OperationCreate
        orm_mode = True

class OperationOut(OperationCreate):
    id: int

    class Config:
        # Configuration options specific to OperationOut
        orm_mode = True

class TopicCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to TopicCreate
        orm_mode = True

class TopicOut(TopicCreate):
    id: int

    class Config:
        # Configuration options specific to TopicOut
        orm_mode = True

class PlaceCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to PlaceCreate
        orm_mode = True

class PlaceOut(PlaceCreate):
    id: int

    class Config:
        # Configuration options specific to PlaceOut
        orm_mode = True

class ProverbCreate(BaseModel):
    english: str
    turkish: str
    examples: str = None

    class Config:
        # Configuration options specific to ProverbCreate
        orm_mode = True

class ProverbOut(ProverbCreate):
    id: int

    class Config:
        # Configuration options specific to ProverbOut
        orm_mode = True