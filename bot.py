import asyncio
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
from handlers import router as handlers_router

load_dotenv()

session = AiohttpSession(proxy="http://proxy.server:3128")


TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(handlers_router)


# Run the bot
async def main() -> None:
    # bot = Bot(token=TOKEN)

    bot = Bot(token=TOKEN, session = session)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
