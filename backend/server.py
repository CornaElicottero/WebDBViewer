import uvicorn
import bcrypt
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request, Depends, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from strawberry.fastapi import GraphQLRouter
from sql_app import schemas, database
from sql_app .database import SessionLocal
from typing import Union, Any, List
from fastapi.params import Query, Header
from dotenv import load_dotenv
import strawberry
from strawberry.asgi import GraphQL
database.Base.metadata.create_all(bind=database.engine)
load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

schema = strawberry.Schema(query=schemas.Query)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)