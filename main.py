import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.url_router import router
from app.settings import IS_LOCAL_INSTANCE

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

@app.get("/")
async def home():
    return "Welcome to URL shortener"

if __name__ == "__main__":
    
    if IS_LOCAL_INSTANCE:
        uvicorn.run(app="main:app", host="127.0.0.1", reload=True)
    else:
        uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
