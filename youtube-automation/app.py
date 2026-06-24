from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import subprocess

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
    request: Request,
    title: str = Form(...),
    category: str = Form(...),
    script: str = Form(...)
):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    script_file = f"scripts/{timestamp}.txt"
    audio_file = f"audio/{timestamp}.wav"

    with open(script_file, "w") as f:
        f.write(script)

    command = f"""
cat {script_file} | \
/home/rocky/youtube-project/piper/piper/piper \
--model /home/rocky/youtube-project/piper/models/en_US-lessac-medium.onnx \
--output_file {audio_file}
"""

    subprocess.run(command, shell=True)

    return HTMLResponse(f"""
    <h2>Audio Generated Successfully</h2>

    <p>Title: {title}</p>

    <p>Category: {category}</p>

    <p>Audio File:</p>

    <pre>{audio_file}</pre>

    <a href="/">Back</a>
    """)
