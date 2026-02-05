from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ ᴡєʟᴄσϻє ᴛᴏ ᴛєᴧϻ ᴋʀɪʀɪ ʀєᴘσs ❃</u>
 
✼ ʀєᴘᴏ ɪs ηᴏᴡ ᴘʀɪᴠᴧᴛє ᴅᴜᴅє 😌
 
❉  ʏᴏᴜ ᴄᴧη ᴜsє мʏ ᴘᴜʙʟɪᴄ ʀєᴘσs !!  

✼ || [˹Ꭰʀᴀᴍᴀ 𝑋˼ 💞](https://t.me/dramaX_view) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜєʟᴘ •", url="https://t.me/anime_helixx"),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url="https://t.me/dramaX_view"),
          ],
[
InlineKeyboardButton("• ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ •", url=f"https://t.me/aniweb_shogunate"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
