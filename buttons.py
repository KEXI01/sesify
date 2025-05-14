from telethon import Button

class Data:
    generate_single_button = [Button.inline("ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ✨", data="generate")]

    home_buttons = [
        generate_single_button,
        [Button.inline("« ʙᴀᴄᴋ", data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            Button.url("ᴀᴘɪ & ʜᴀꜱʜ", url="https://my.telegram.org/auth"),
            Button.url("ɢᴇɴᴇʀᴀᴛᴇ ᴏɴʟɪɴᴇ", url="https://telegram.tools/session-string-generator#pyrogram,user")
        ],
        [
            Button.url("ꜱᴜᴘᴘᴏʀᴛ 🍁", url="https://t.me/STORM_CORE")
        ],
    ]
