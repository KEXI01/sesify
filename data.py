from pyrogram.types import InlineKeyboardButton
from pyrogram.types import WebAppInfo


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ✨", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="« ʙᴀᴄᴋ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("ᴀᴘɪ & ʜᴀꜱʜ", web_app=WebAppInfo(url="https://my.telegram.org/auth")),
            InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴏɴʟɪɴᴇ", web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user"))
        ],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ❔", callback_data="help")
        ],
        [
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ❄️", url="https://t.me/STORM_CORE"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ 🍁", url="https://t.me/STORM_TECHH")
        ],
    ]

    START = """
<blockquote><b>ʜᴇʏ 💐</b>
<b>ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ,
1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ</b></blockquote>
<blockquote><b>ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ <a href="https://envs.sh/odM.mp4">?</a>
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀꜱɪᴏɴ 2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ</b></blockquote>
<blockquote><b>ʙʏ @STORM_CORE ☁️</b></blockquote>
    """

    HELP = """
<blockquote><b>✨ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ✨</b></blockquote>
<blockquote><b>/help - ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
/start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ
/restart - ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ</b></blockquote>
"""

