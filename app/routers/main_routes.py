from fastapi import APIRouter, Request

app = APIRouter()

@app.get("/")
async def root(
    request: Request
):
    html_templates = request.app.state.templates
    return html_templates.TemplateResponse("index.html", {"request": request})