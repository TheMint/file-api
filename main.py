"""
VAST Data Infra Team - Home Exercise

Filesystem CRUD REST server.
Uses FastAPI and uvicorn for ASGI.

Asynchronious fs operations are performed by aiofiles, see implementation below.
Swagger available at /docs, if you're interested in playing with it yourself.

by Yotam Ran
"""

import os
import uvicorn
import aiofiles
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from utils import check_if_file_exists, check_if_dir_exists

app = FastAPI()


@app.get("/readFile")
async def readFile(file_path: str) -> JSONResponse:
    check_if_file_exists(file_path)
    try:
        async with aiofiles.open(file_path, "r") as f:
            content = await f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content={"filename": file_path, "content": content})


@app.get("/updateFile")
async def updateFile(file_path: str, content: str) -> JSONResponse:
    check_if_file_exists(file_path)
    try:
        async with aiofiles.open(file_path, "w") as f:
            await f.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content={"msg": "Updated file"}, status_code=200)


@app.get("/deleteFile")
async def deleteFile(file_path: str) -> JSONResponse:
    check_if_file_exists(file_path)
    try:
        os.remove(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content={"msg": "Removed file"}, status_code=200)


@app.get("/createFile")
async def createFile(file_path: str) -> JSONResponse:
    try:
        async with aiofiles.open(file_path, "w") as f:
            f.write("")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content={"msg": f"Created file {file_path}"}, status_code=200)


@app.get("/listDir")
async def listDir(dir_path: str) -> JSONResponse:
    check_if_dir_exists(dir_path)
    try:
        fileList = os.listdir(path=dir_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content={"dir": dir_path, "files": fileList}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
