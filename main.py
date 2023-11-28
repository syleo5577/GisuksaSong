from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import db_functions as db
import link_functions as link

class linkInput(BaseModel):
    url: str

class DataStorage(BaseModel):
    data: list[list]

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 허용할 도메인들
    allow_credentials=True,
    allow_methods=["*"],  # 허용할 HTTP 메소드
    allow_headers=["*"],  # 허용할 HTTP 헤더
)




@app.get("/main")
async def root(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get("/main/data")
async def get_item():
    data = db.getDataWithoutDeleted(0)
    return {"data": data}  # GET 요청시 저장된 데이터를 반환합니다.

@app.post("/main")
async def create_item(item: linkInput):
    print(item)
    return {"value": item.url}