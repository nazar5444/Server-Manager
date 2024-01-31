import asyncio
import logging
import subprocess
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

TOKEN = "6812143726:AAGV6bIx0SgZ3QKsQ9KhymK2nm3Z2_sIIeI"
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("exec"))
async def command_handler(message: Message) -> None:
    if message.from_user.id == 629888234:  # Replace YOUR_USER_ID with your actual ID
        command = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
        if command:
            try:
                result = subprocess.check_output(command, shell=True, text=True)
                await message.reply(f"Command executed successfully:\n```\n{result}\n```",
                                    parse_mode=ParseMode.MARKDOWN)
            except subprocess.CalledProcessError as e:
                await message.reply(f"Error executing command:\n```\n{e}\n```", parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply("Please provide a command to execute.")
    else:
        await message.reply("You are not authorized to execute commands.")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())