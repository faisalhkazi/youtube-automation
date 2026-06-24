from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/generate")
async def generate(
    title: str = Form(...),
    category: str = Form(...),
    script: str = Form(...)
):
    return {
        "title": title,
        "category": category,
        "script_length": len(script)
    }
