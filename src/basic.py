from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(
        msg.chat.id,
    f"<blockquote><b>ʜᴇʏ 💐</b>\n"
    f"<b>ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ,</b>\n"
    f"<b>1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ</b>\n"
    f"<b>2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ</b></blockquote>\n"
    f"<blockquote><b>ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ <a href='https://envs.sh/o2o.mp4'>?</a></b>\n"
    f"<b>ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴠ2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ.</b>\n"
    f"<b>ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ</b></blockquote>\n"
    f"<blockquote><b>ʙʏ @STORM_CORE ☁️</b></blockquote>",
    reply_markup=InlineKeyboardMarkup(Data.buttons),
    parse_mode="html"
)  # <- This closing parenthesis was missing


@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id, Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
