from fastapi import FastAPI
from database import Base, engine
import endpoints
import models



#create the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Turkish Language API",
    description = """
    This is an api based on the book Lexicarry. The api allows  
    the user to search 7 different categories (e.g. Functions, Sequences, etc.) 
    and return the data for the specific category searched. 
    The search is made in English and returns a dictionary of the 
    category searched.

    """

)

#Router from endpoints.py
app.include_router(endpoints.router)





