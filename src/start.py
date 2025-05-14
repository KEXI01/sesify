"""from telethon import events, Button
from buttons import Data

@client.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def start(event):
    me = await client.get_me()
    mention = f'<a href="tg://user?id={me.id}">{me.first_name}</a>'
    
    await event.respond(
        f"<blockquote><b>ʜᴇʏ 💐</b>\n"
        f"<b>ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ,</b>\n"
        f"<b>1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ</b>\n"
        f"<b>2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ</b></blockquote>\n"
        f"<blockquote><b>ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ <a href='https://envs.sh/o2o.mp4'>?</a></b>\n"
        f"<b>ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴠ2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ.</b>\n"
        f"<b>ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ</b></blockquote>\n"
        f"<blockquote><b>ʙʏ @STORM_CORE ☁️</b></blockquote>",
        parse_mode='html',
        buttons=Data.buttons  # Ensure these are Telethon buttons
    )"""
