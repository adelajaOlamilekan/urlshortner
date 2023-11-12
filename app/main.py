import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.url_router import router

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

"""if __name__ == "__main__":
    uvicorn.run(app="app.main", port=8000, reload=True)"""

