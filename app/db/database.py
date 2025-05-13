from tortoise import Tortoise
from core.config import settings


async def init_db():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={'models': ['app.db.models']}
    )
    await Tortoise.generate_schemas()
