from app.db.models import SpotX  # путь подправь под себя
from app.db.schemas.spotx import SpotXCreateSchema


async def add_token_if_not_exists(data: SpotXCreateSchema):
    existing = await SpotX.filter(token=data.token).first()
    print(existing)
    if not existing:
        print(1)
        await SpotX.create(token=data.token, end_at=data.end_at)
        print(f"Token '{data.token}' добавлен.")
    else:
        print(f"Token '{data.token}' уже существует.")
