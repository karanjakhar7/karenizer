from fastapi import APIRouter, Request

app = APIRouter()


@app.get("/")
async def index(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(request, "index.html")
