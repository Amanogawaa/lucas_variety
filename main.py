from fastapi import FastAPI
from api.controllers import auth_controller
from api.middleware import cors_middleware


def create_app() -> FastAPI:
    app = FastAPI()

    origins = [
        "http://localhost",
        "http://localhost:5173",
    ]

    cors_middleware.add(app)

    app.include_router(auth_controller.router, prefix="/api")

    return app


app = create_app()
