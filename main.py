from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

app = FastAPI()

# CORS를 활성화하고 모든 도메인을 허용합니다.
# 모든 출발지를 허용하고 필요한 경우 특정 출발지를 설정하세요.
# 프로덕션 환경에서는 보안 위험을 완화하기 위해 특정 출발지만 허용해야 합니다.
# allow_origin=["*"] 을  http://localhost:3000 같이 특정 도메인만 허용할 수 있습니다.
origins = [
    "http://localhost:60285",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def index():
    return FileResponse("web/index.html")

@app.get("/hello")
def hello():
    return {"message": "안녕하세요"}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/web", StaticFiles(directory="web"))

# uvicorn main:app --reload