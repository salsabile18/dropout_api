import io

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import pickle
import pandas as pd
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# Montez le répertoire statique pour servir des fichiers statiques
app.mount("/static", StaticFiles(directory="templates/static"), name="static")

est = pickle.load(open("modele_entraîné.pkl", "rb"))


# Définir une route pour le fichier favicon.ico
#@app.get("/favicon.ico")
#async def get_favicon():
#   return FileResponse("static/favicon.ico")


@app.get('/flask', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("Frontend.html", {"request": request})


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("Frontend.html", {"request": request})


@app.get('/js/{path}')
async def send_js(path: str):
    return FileResponse("templates/static/" + path)


@app.post('/predict')
async def predict(request: Request, file: UploadFile = File(...)):
    # Laissez la logique de gestion des erreurs à FastAPI
    contents = (await file.read()).decode('utf-8')
    df = pd.read_csv(io.StringIO(contents))
    predictions = est.predict(df)
    proba_predictions = est.predict_proba(df)[:, 1]

    # Ajouter les autres colonnes au dataframe des résultats
    df['prediction'] = predictions
    df['probability'] = proba_predictions

    # Convertir les valeurs int64 en int
    df['prediction'] = df['prediction'].astype(int)

    # Convertir le dataframe en liste de dictionnaires
    results = df.to_dict(orient='records')
    return results



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002, reload=True)

