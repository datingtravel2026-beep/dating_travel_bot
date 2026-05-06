from app.database.db import SessionLocal
from app.database.models import User
from sqlalchemy import select


async def get_user(telegram_id: int):
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()


async def create_user(telegram_id: int):
    async with SessionLocal() as session:
        user = User(telegram_id=telegram_id)
        session.add(user)
        await session.commit()
        return user


async def update_user(telegram_id: int, **kwargs):
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one()

        for key, value in kwargs.items():
            setattr(user, key, value)

        await session.commit()
