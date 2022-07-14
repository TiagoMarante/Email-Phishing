# Local development template FastApi 
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![requirements](https://img.shields.io/requires/github/boooka/fastapi)](https://img.shields.io/requires/github/boooka/fastapi)
[![last-commit](https://img.shields.io/github/last-commit/boooka/fastapi)](https://github.com//boooka/fastapi)

A vary simple template for bootstrapping a FastAPI. 
## Why?

A surprisingly interesting framework that interested me with detailed documentation that you will find at [FastAPI official
docs](https://fastapi.tiangolo.com/). Uses a lot of modern features of the python. Here is a set of files that allow you to start using FastAPI in a couple of commands. 

**FastAPI**: https://github.com/tiangolo/fastapi

---

## Quick Start

Install requirements, run

```bash
pip install requirements.txt
uvicorn app.main:app --reload
```

## Setup
You don't need to install localy env, you can use one of the follow docker images as yours env

Use docker-compose, docker or direct bash script:
#### docker-compose
Install docker-compose if you don't already have it:

[docker-compose installation official
docs](https://docs.docker.com/compose/install/).

Dockerfile use multistage build.
Then, in the directory you want your project to live:

```bash
docker-compose up -d
```

#### docker

```bash
docker build --rm -t fast-api:latest .
docker run -d --name fast-api -p 8000:8000 fast-api
```

also you can use build.sh, keep in mind that's script remove images after stop:
```bash
./build.sh
```

#### command line run
if this, than you should install env localy^

```bash
python -m venv ./venv
source ./venv/bin/activate
pip install requirements.txt
uvicorn app.main:app --reload
```

## Blank page 

Once this finishes you can navigate to (default is
`localhost:8000`), you should see same response

## API docs

FastAPI provide from the box documenation based on OpenAPI standart swagger and redoc

`localhost:8000/docs` or 
`localhost:8000/docs/redoc`




