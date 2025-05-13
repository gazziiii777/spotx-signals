from app.db.models import SpotX  # путь подправь под себя


async def add_token_if_not_exists(token: str):
    existing = await SpotX.filter(token=token).first()
    if not existing:
        await SpotX.create(token=token)
        print(f"Token '{token}' добавлен.")
    else:
        print(f"Token '{token}' уже существует.")
