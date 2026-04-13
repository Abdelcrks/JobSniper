from fastapi import FastAPI
from database import engine, Base
import models.offer
import models.profile
import models.project
import models.skill
import models.generation

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}