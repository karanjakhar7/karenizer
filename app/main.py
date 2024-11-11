import os
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from .routers import apis, main_routes

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.state.templates = templates


origins = [
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(apis.router)
app.include_router(main_routes.app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
