from fastapi import FastAPI
from pathlib import Path
import uvicorn

app = FastAPI()


@app.get("/readFile")
async def readFile(file_path: str):

    return {"msg": "hello world"}


@app.get("/writeFile")
async def writeFile(content: str):
    return {"msg": "hello world"}


@app.get("/deleteFile")
async def deleteFile(file_path: str):
    return {"msg": "hello world"}


@app.get("/createFile")
async def readFile():
    return {"msg": "hello world"}


@app.get("/listDir")
async def readFile():
    return {"msg": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
