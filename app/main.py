from fastapi import FastAPI
from .database import engine
from . import models

app = FastAPI()

