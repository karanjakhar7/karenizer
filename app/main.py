from fastapi import FastAPI
from .routers import main_routes

app = FastAPI()

app.include_router(main_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
