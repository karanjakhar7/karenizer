from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from .routers import apis, main_routes

app = FastAPI(
    title="Karenizer",
    description="Transform grievances into legendary Karen-level complaint letters.",
    version="1.0.0",
)

# Use __file__-relative path so templates resolve correctly on Vercel and locally
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
app.state.templates = templates

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apis.router)
app.include_router(main_routes.app)
