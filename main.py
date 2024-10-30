from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Base, engine
from sqlalchemy.orm import Session
from typing import List
import endpoints
from endpoints import get_db
import models
import json



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

#connecting FastApi with static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

#connecting FastApi with templates folder
templates = Jinja2Templates(directory="templates")

#Router from endpoints.py
app.include_router(endpoints.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    functions = db.query(models.Functions).all()  # Fetch all functions from the database
    functions_json = json.dumps([  # Convert functions to JSON-like format
        {
            "id": func.id,
            "english": func.english,
            "turkish": func.turkish,
            "examples": [example.strip() for example in func.examples.split(",")] if func.examples else []  # Split by comma and strip whitespace
        }
        for func in functions
    ], ensure_ascii=False, indent=4)
    return templates.TemplateResponse("index.html", {"request": request, "functions": functions, "functions_json": functions_json})









