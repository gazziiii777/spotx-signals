from aiogram import Router, F, types, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.services.parcer import BybitListingFetcher
from app.db.data_access import add_token_if_not_exists
import asyncio
from datetime import datetime, timezone, timedelta
from app.db.schemas.spotx import SpotXCreateSchema


router = Router()


async def time_convert(timestamp_seconds: int):
    utc_time = datetime.fromtimestamp(timestamp_seconds, tz=timezone.utc)
    msk_time = utc_time.astimezone(timezone(timedelta(hours=3)))
    return msk_time


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("asda")
    fetcher = BybitListingFetcher()
    # while True:
    try:
        data = await fetcher.get_listings()
        for item in data:
            end_at = await time_convert(item.get("projectEndTime")/1000)
            data = SpotXCreateSchema(
                token=item.get("token"),
                end_at=end_at
            )
            if await add_token_if_not_exists(data):
                await message.answer(item.get("token"))
        await asyncio.sleep(1800)
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        return None
