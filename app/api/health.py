from fastapi import APIRouter

from app.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Report application readiness without contacting optional services."""
    settings = get_settings()
    return {
        "status": "ok",
        "application": settings.app_name,
        "environment": settings.environment,
    }
