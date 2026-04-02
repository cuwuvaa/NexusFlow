from fastapi import FastAPI

from nexusflow.api.router import router as api_router
from nexusflow.core.config import get_settings
from nexusflow.core.logging import configure_logging


def create_app() -> FastAPI:
    configure_logging()
    settings = get_settings()

    app = FastAPI(title=settings.app_name)
    app.include_router(api_router)
    return app


app = create_app()
