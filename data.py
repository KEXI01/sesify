from pyrogram.types import InlineKeyboardButton
from pyrogram.types import WebAppInfo


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ✨", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("ᴀᴘɪ & ʜᴀꜱʜ", web_app=WebAppInfo(url="https://my.telegram.org/auth")),
            InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ ᴏɴʟɪɴᴇ", web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user"))
        ],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ 🎪", callback_data="about"),
            InlineKeyboardButton("ꜱᴇꜱꜱɪᴏɴ ᴀɴᴀʟʏᴢᴇʀ", web_app=WebAppInfo(url="https://telegram.tools/session-string-analyzer"))
        ],
        [InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ❄️", url="https://t.me/STORM_CHATZ")],
    ]

    START = """
ʜᴇʏ 💐

ᴡᴇʟᴄᴏᴍᴇ {}

ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ,
1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ 

ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀꜱɪᴏɴ 2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

ʙʏ @STORM_CHATZ ☁️
    """

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ** ✨

/ᴀʙᴏᴜᴛ - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/ʜᴇʟᴘ - ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
/ꜱᴛᴀʀᴛ - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/ɢᴇɴᴇʀᴀᴛᴇ - ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ
/ᴄᴀɴᴄᴇʟ - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ
/ʀᴇꜱᴛᴀʀᴛ - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ
"""

    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ**

ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙʏ @STORM_CHATZ

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : [Kᴜɴᴀʟ ᶻ 𝘇 𐰁](https://t.me/kexx_xd)
    """
