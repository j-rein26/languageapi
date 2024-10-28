from fastapi import FastAPI
from database import Base, engine
import endpoints
import models



#create the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Router from endpoints.py
app.include_router(endpoints.router)





