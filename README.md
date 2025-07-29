# lolmob Backend

This repository provides a minimal REST API built with [FastAPI](https://fastapi.tiangolo.com/).

## Features

- SQLAlchemy models for leagues, teams and players
- Service layer with dedicated routers for leagues and teams
- Database URL configurable via the `DATABASE_URL` environment variable
- `uvicorn` entrypoint defined in `codex.yaml`

## Running the Application

Install dependencies and start the server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` with interactive docs at `/docs`.
