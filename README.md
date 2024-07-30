# VAST Data Infra Team - Home Exercise

Filesystem CRUD REST server.
Uses FastAPI and uvicorn for ASGI.

Asynchronious fs operations are performed by aiofiles, see implementation below.
Swagger available at /docs, if you're interested in playing with it yourself.


## Docker usage
Build local image -
```
docker build -t yotam-server .
```

Run - 
```
docker run -p 8000:8000 yotam-server
```


## Authors

- [@Yotam Ran](https://github.com/TheMint)
