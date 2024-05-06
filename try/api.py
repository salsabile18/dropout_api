import uvicorn
from fastapi import FastAPI, Form, Request
import pickle
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

app = FastAPI()

model = pickle.load(open('modele_entraîné.pkl', 'rb'))
predictions_classes = {0: "Non-Décrocheur", 1: "Décrocheur"}
templates = Jinja2Templates(directory="templates")




@app.get("/")
async def login_page(request: Request):
    return templates.TemplateResponse("app.html", {"request": request})


@app.post("/login/")
async def login(
        request: Request,
        typeEnseignement: int = Form(...),
        NbrRedoublement: int = Form(...),
        MoyenneNotes: float = Form(...),
        id_Genre: int = Form(...),
        Age: int = Form(...),
        CD_REG: int = Form(...),
        cd_com: int = Form(...),
        CD_MIL: int = Form(...),
        suffix_index: int = Form(...)
):
    inf_features = [
        [typeEnseignement, NbrRedoublement, MoyenneNotes, id_Genre, Age, CD_REG, cd_com, CD_MIL, suffix_index]]

    # Prédire la classe et la probabilité de décrochage
    results = model.predict(inf_features)
    prediction_proba = model.predict_proba(inf_features)[:, 1]  # Probabilité de décrochage

    # Récupérer la prédiction de classe (0 ou 1)
    results = results.tolist()[0]
    prediction_result = predictions_classes[results]

    # Créer une réponse JSON avec la prédiction de classe et la probabilité de décrochage
    response = {
        "prediction_result": prediction_result,
        "pourcentage_decrochage": float(prediction_proba[0]) * 100  # Convertir la probabilité en pourcentage
    }

    return JSONResponse(content=response)


# Endpoint pour typeEnseignement
@app.get("/typeEnseignement/{typeEnseignement}")
async def get_typeEnseignement(typeEnseignement: int):
    return JSONResponse(content={"typeEnseignement": typeEnseignement})

# Endpoint pour NbrRedoublement
@app.get("/NbrRedoublement/{NbrRedoublement}")
async def get_NbrRedoublement(NbrRedoublement: int):
    return JSONResponse(content={"NbrRedoublement": NbrRedoublement})

# Endpoint pour MoyenneNotes
@app.get("/MoyenneNotes/{MoyenneNotes}")
async def get_MoyenneNotes(MoyenneNotes: float):
    return JSONResponse(content={"MoyenneNotes": MoyenneNotes})


# Endpoint pour id_Genre
@app.get("/id_Genre/{id_Genre}")
async def get_id_Genre(id_Genre: int):
    return JSONResponse(content={"id_Genre": id_Genre})

# Endpoint pour Age
@app.get("/Age/{Age}")
async def get_Age(Age: int):
    return JSONResponse(content={"Age": Age})

# Endpoint pour CD_REG
@app.get("/CD_REG/{CD_REG}")
async def get_CD_REG(CD_REG: int):
    return JSONResponse(content={"CD_REG": CD_REG})

# Endpoint pour cd_com
@app.get("/cd_com/{cd_com}")
async def get_cd_com(cd_com: int):
    return JSONResponse(content={"cd_com": cd_com})

# Endpoint pour CD_MIL
@app.get("/CD_MIL/{CD_MIL}")
async def get_CD_MIL(CD_MIL: int):
    return JSONResponse(content={"CD_MIL": CD_MIL})

# Endpoint pour suffix_index
@app.get("/suffix_index/{suffix_index}")
async def get_suffix_index(suffix_index: int):
    return JSONResponse(content={"suffix_index": suffix_index})


#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)