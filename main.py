from fastapi import FastAPI
from database import engine, Base
import models.offer
import models.profile
import models.project
import models.skill
import models.generation
from routers.offers import router as offers_router
from routers.profiles import router as profiles_router
from routers.generations import router as generations_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(offers_router)
app.include_router(profiles_router)
app.include_router(generations_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}