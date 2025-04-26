from fastapi import FastAPI
from src.routers import challenges

app = FastAPI(
    title='ogathon-challenges-api',
    description='Api de Codevergence para el reto de Ogathon',
    version='1.0.0',
    docs_url='/swagger',
)

app.include_router(challenges.router)