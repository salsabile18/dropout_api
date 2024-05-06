import subprocess

import uvicorn
from flask import Flask
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Démarrer les serveurs FastAPI en tant que processus séparés
fastapi_process = subprocess.Popen(["uvicorn", "appi1:app", "--host", "127.0.0.1", "--port", "8001"])
flask_process = subprocess.Popen(["uvicorn", "appi2:app", "--host", "127.0.0.1", "--port", "8002"])


app = FastAPI()
templates = Jinja2Templates(directory="templates")


# appp = Flask(__name__)


@app.get("/fastapi")
async def redirect_to_fastapi():
    #    uvicorn.run(app, host="127.0.0.1", port=8001)
    return RedirectResponse(url="http://127.0.0.1:8001/fastapi")


@app.get("/flask")
async def redirect_to_fastapi():
    return RedirectResponse(url="http://127.0.0.1:8002/flask")


# @appp.route('/flask')
# def flask_route()
#    return RedirectResponse(url="http://127.0.0.1:8001/fastapi")

@app.get("/", response_class=HTMLResponse)
async def select_api(request: Request):
    return templates.TemplateResponse("select_api.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
