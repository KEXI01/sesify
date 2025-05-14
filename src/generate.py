from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

from pyrogram.types import WebAppInfo
from data import Data


ask_ques = "<blockquote><b>ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ</b></blockquote>"

buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram_menu"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon_menu"),
    ],
    [
        InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="home")        
    ]
]

pyrogram_menu_buttons = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ᴜꜱᴇʀ", callback_data="pyrogram"),
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
    ],
    [
        InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="generate")
    ]
]

telethon_menu_buttons = [
    [
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ᴜꜱᴇʀ", callback_data="telethon"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
    [
        InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="generate")
    ]
]

@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.edit(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))

@Client.on_message(filters.private & ~filters.forwarded & filters.command('pyrogram'))
async def main(_, msg):
    await msg.edit(reply_markup=InlineKeyboardMarkup(pyrogram_menu_buttons))    

@Client.on_message(filters.private & ~filters.forwarded & filters.command('telethon'))
async def main(_, msg):
    await msg.edit(reply_markup=InlineKeyboardMarkup(telethon_menu_buttons))    


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "ᴛᴇʟᴇᴛʜᴏɴ"
    else:
        ty = "ᴘʏʀᴏɢʀᴀᴍ ᴠ2"
    if is_bot:
        ty += "ʙᴏᴛ"
    await msg.reply(f"<blockquote><b>ꜱᴛᴀʀᴛɪɴɢ . . . {ty} ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛɪᴏɴ . . .</b></blockquote>")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, '<blockquote><b>ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ ᴀᴘɪ ɪᴅ</b></blockquote>', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('<blockquote><b>ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ᴀᴘɪ_ɪᴅ (ᴡʜɪᴄʜ ᴍᴜꜱᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ). ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, '<blockquote><b>ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ ᴀᴘɪ ʜᴀꜱʜ</b></blockquote>', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "<blockquote><b>ɴᴏᴡ ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ. \nᴇxᴀᴍᴘʟᴇ : `+19876543210`</b></blockquote>'"
    else:
        t = "<blockquote><b>ɴᴏᴡ ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ \nᴇxᴀᴍᴘʟᴇ : `12345:abcdefghijklmnopqrstuvwxyz`</b></blockquote>'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("<blockquote><b>ꜱᴇɴᴅɪɴɢ ᴏᴛᴘ...</b></blockquote>")
    else:
        await msg.reply("<blockquote><b>ʟᴏɢɢɪɴɢ ᴀꜱ ʙᴏᴛ ᴜꜱᴇʀ...</b></blockquote>")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('<blockquote><b>ᴀᴘɪ ɪᴅ ᴀɴᴅ ᴀᴘɪ ʜᴀꜱʜ ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('<blockquote><b>ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "<blockquote><b>ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ꜰᴏʀ ᴀɴ ᴏᴛᴘ ɪɴ ᴏꜰꜰɪᴄɪᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ. ɪꜰ ʏᴏᴜ ɢᴏᴛ ɪᴛ, ꜱᴇɴᴅ ᴏᴛᴘ ʜᴇʀᴇ ᴀꜰᴛᴇʀ ʀᴇᴀᴅɪɴɢ ᴛʜᴇ ʙᴇʟᴏᴡ ꜰᴏʀᴍᴀᴛ. \nɪꜰ ᴏᴛᴘ ɪꜱ `12345`, **ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ɪᴛ ᴀꜱ** `1 2 3 4 5`.</b></blockquote>", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('<blockquote><b>ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 10 ᴍɪɴᴜᴛᴇꜱ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('<blockquote><b>ᴏᴛᴘ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('<blockquote><b>ᴏᴛᴘ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ</b></blockquote>', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '<blockquote><b>ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ ᴇɴᴀʙʟᴇᴅ ᴛᴡᴏ-ꜱᴛᴇᴘ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ. ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴘᴀꜱꜱᴡᴏʀᴅ.</b></blockquote>', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('<blockquote><b>ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴᴜᴛᴇꜱ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('<blockquote><b>ɪɴᴠᴀʟɪᴅ ᴘᴀꜱꜱᴡᴏʀᴅ ᴘʀᴏᴠɪᴅᴇᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴀɢᴀɪɴ.</b></blockquote>', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"<blockquote><b>{ty.upper()} ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ \n\n`{string_session}`</b></blockquote>"
    try:
        if not is_bot:
            await bot.send_message(msg.chat.id, text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "<blockquote><b>ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ {} ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ.</b></blockquote>".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("<blockquote><b>ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ!</b></blockquote>", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("<blockquote><b>ʀᴇꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ!</b></blockquote>", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):
        await msg.reply("<blockquote><b>ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ!</b></blockquote>", quote=True)
        return True
    else:
        return False
