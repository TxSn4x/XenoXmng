import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from SONALI_MUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("`/git TEAMKRITI`")
        return

    username = message.text.split(None, 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
                caption = f"""ɪᴅʜᴀʀ ᴀᴀ ʙᴋʟ ᴛᴜJᴇ ᴍᴇ ᴅᴇᴛᴀ ʜᴜ ɪɴғᴏ ɢɪᴛʜᴜʙ
             except Exception as e:
                print(str(e))
                pass

    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("Close", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)
