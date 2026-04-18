from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from pydantic import BaseModel
# import sqlite3
# from sqlite3 import Connection
# from pathlib import Path

from app.hasPath import Graph

# DB_PATH = Path("db_sqlite3")
# SCRIPT_PATH = Path("schema.sql")

app = FastAPI(title = "Exchange App", version="1.0.0")

# class Currency(BaseModel):
#     currency_id: int
#     currency: str

# class Conversion(BaseModel):
#     currency_id: int
#     conversion_currency: str

# def get_db():
#     try:
#         with sqlite3.connect(DB_PATH, check_same_thread=False) as connection:
#             connection.executescript("schema.sql")
#             connection.row_factory = sqlite3.Row
#             yield connection
#     except HTTPException as e:
#         raise e(500, "Unable to connect to database server")

class RequestModel(BaseModel):
    edges: list[list[str]]

class Response(BaseModel):
    pathExists: bool

class HealthCheck(BaseModel):
    status: str = "ok"
    
   
@app.get("/", response_model=HealthCheck)
def root():
    return HealthCheck()

@app.post("/has-path", status_code=200, response_model=Response)
def has_path(input: RequestModel, source: str, target: str):
    proccess_execute = Graph(input=input.edges)
    response = proccess_execute.has_path(start=source, end=target)
    return Response(pathExists=response)

# @app.post("/conversion", status_code=201, response_model=Currency)
# def register_conversion(currency: str, conversion: list, db: Connection=Depends(get_db)):
#     try:
#         db.execute("INSERT INTO conversion (currency) VALUES (?)", (currency,))
#         currency_id = db.execute("SELECT last_insert_rowid()")
#         for curr in conversion:
#             db.execute("INSERT INTO conversion (conversion_currency, currency_id) VALUES (?, ?)", (curr, currency_id),)
#         return Currency(**db.execute("SELECT * FROM currency AS curr LEFT JOIN conversion AS conv WHERE curr.currency_id == conv.currency_id ORDER BY curr.currency_id DESC LIMIT 1").fetchone())
#     except HTTPException as ex:
#         raise ex(500, "The system was unable to register the currencies")




