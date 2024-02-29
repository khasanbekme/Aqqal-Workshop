# Credentials to be changed
FLOWISE_API_URL = "PASTE_YOUR_API_URL_HERE"
BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.utils.chat_action import ChatActionSender

bot = Bot(BOT_TOKEN, parse_mode="markdown")
dp = Dispatcher()


async def query(question: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            FLOWISE_API_URL,
            json={"question": question},
        ) as response:
            return await response.json()


@dp.message()
async def echo_handler(message: types.Message) -> None:
    async with ChatActionSender(
        bot=bot, chat_id=message.chat.id, action="typing"
    ):
        try:
            response = await query(message.text)
            await message.answer(response["text"])
        except Exception:
            await message.answer("Something went wrong, try again later.")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
