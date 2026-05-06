import asyncio

from app.config.loader import dp, bot
from app.handlers import start, registration, subscription


async def main():
    dp.include_router(start.router)
    dp.include_router(subscription.router)
    dp.include_router(registration.router)

    # ✅ ВНУТРИ async функции
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
