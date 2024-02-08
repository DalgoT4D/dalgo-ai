# main.py
from fastapi import FastAPI
import uvicorn
import argparse
from routers import train

def create_app():
    app = FastAPI()

    @app.get("/healthcheck")
    def healthcheck():
        return {"status": "ok"}

    app.include_router(train.router)
    return app

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="FastAPI Machine Learning API")
    parser.add_argument("--port", type=int, default=8000, help="Port number to bind the FastAPI application")
    args = parser.parse_args()

    uvicorn.run("main:create_app", host="127.0.0.1", port=args.port, reload=True)
