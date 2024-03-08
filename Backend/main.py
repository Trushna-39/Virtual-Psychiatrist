from fastapi import FastAPI
from router import user
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static", html = True), name="static")

app.include_router(user.router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)