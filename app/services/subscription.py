from aiogram import Bot
from aiogram.enums import ChatMemberStatus

from app.config.settings import CHANNEL_ID, CHAT_ID


async def check_sub(bot: Bot, user_id: int) -> bool:
    try:
        member1 = await bot.get_chat_member(CHANNEL_ID, user_id)
        member2 = await bot.get_chat_member(CHAT_ID, user_id)

        return (
            member1.status in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.CREATOR,
            ]
            and
            member2.status in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.CREATOR,
            ]
        )

    except:
        return False
