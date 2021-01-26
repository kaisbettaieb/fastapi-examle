from fastapi import FastAPI, Response

from pydantic import BaseModel

tags_metadata = [
    {
        "name": "salutations",
        "description": "Simple **endpoint** pour saluer le serveur. xD",
    }
]

app = FastAPI(title="Application pour tester le CI/CD",
              description="Realisations d'une application simple pour tester les outils CI/CD",
              version="0.1", openapi_tags=tags_metadata)


class BaseReponseModele(BaseModel):
    status: str
    message: str


@app.get("/api/0.1/salutations", response_model=BaseReponseModele, tags=["salutations"])
def salutation(response: Response):
    response.status_code = 200
    return {"status": "Success", "message": "Salut, J'espère que vous allez bien."}


@app.get("/")
def index(response: Response):
    response.status_code = 200
    return {"url": "/docs", "message": "pour visualiser l'interface SwaggerUI"}
