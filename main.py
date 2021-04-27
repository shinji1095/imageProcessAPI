from fastapi import FastAPI
import os, sys
appendFile = os.path.join(os.path.dirname(__file__), "controllers")
print(appendFile)
sys.path.append(appendFile)
from ImageController import test

app = FastAPI()

test()

@app.get("/")
async def root():
    return {"message": "Hello World"}