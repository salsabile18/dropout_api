import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
import pickle
import pandas as pd
from starlette.responses import FileResponse
from starlette.requests import Request

app = FastAPI()

est = pickle.load(open("modele_entraîné.pkl", "rb"))


@app.get('/')
def home():
    return {"message": "Welcome to my FastAPI!"}


@app.get('/flask')
def index():
    return FileResponse("templates/Frontend.html")


@app.get('/js/{path}')
def send_js(path: str):
    return FileResponse("templates/static/" + path)


@app.post('/predict')
async def predict(request: Request, file: UploadFile = File(...)):
    if est is None:
        raise HTTPException(status_code=500, detail='Model not loaded')

    try:
        contents = await file.read()
        df = pd.read_csv(contents)
        predictions = est.predict(df)
        proba_predictions = est.predict_proba(df)[:, 1]

        # Convertir les valeurs int64 en int
        predictions = predictions.astype(int)

        results = [{'prediction': int(pred), 'probability': proba} for pred, proba in
                   zip(predictions, proba_predictions)]
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
