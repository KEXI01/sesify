import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from StringSessionBot.generate import generate_session, ask_ques, buttons_ques, pyrogram_menu_buttons, telethon_menu_buttons


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    mention = user.mention
    query = callback_query.data
    try:
        if query.startswith("home"):
            if query == 'home':
                chat_id = callback_query.from_user.id
                message_id = callback_query.message.id
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text=Data.START.format(callback_query.from_user.mention, mention),
                    reply_markup=InlineKeyboardMarkup(Data.buttons),
                )
        elif query == "about":
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.ABOUT,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.home_buttons),
            )
        elif query == "help":
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.home_buttons),
            )
        elif query == "generate":
            await callback_query.answer()
            await callback_query.message.edit(
                text=ask_ques,
                reply_markup=InlineKeyboardMarkup(buttons_ques)
            )
        elif query == "pyrogram_menu":
            await callback_query.answer()
            await callback_query.message.edit(
                text=ask_ques,
                reply_markup=InlineKeyboardMarkup(pyrogram_menu_buttons)
            )
        elif query == "telethon_menu":
            await callback_query.answer()
            await callback_query.message.edit(
                text=ask_ques,
                reply_markup=InlineKeyboardMarkup(telethon_menu_buttons)
            )
        elif query in ["pyrogram", "pyrogram_bot", "telethon", "telethon_bot"]:
            try:
                if query == "pyrogram":
                    await generate_session(bot, callback_query.message)
                elif query == "pyrogram_bot":
                    await callback_query.answer("Please note that this bot session will be of pyrogram v2", show_alert=True)
                    await generate_session(bot, callback_query.message, is_bot=True)
                elif query == "telethon":
                    await callback_query.answer()
                    await generate_session(bot, callback_query.message, telethon=True)
                elif query == "telethon_bot":
                    await callback_query.answer()
                    await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            except Exception as e:
                await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
                print(traceback.format_exc())
                print(e)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        await callback_query.message.reply("An error occurred while processing your request.")


ERROR_MESSAGE = """ᴏᴏᴘꜱ! ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀʀᴇᴅ! 
**ᴇʀʀᴏʀ** : {} 

ᴘʟᴇᴀꜱᴇ ᴠɪꜱɪᴛ @rasedidstore ɪꜰ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴅᴏᴇꜱɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ ꜱᴇɴꜱɪᴛɪᴠᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ʏᴏᴜ ɪꜰ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴛʜɪꜱ ᴀꜱ ᴛʜɪꜱ ᴇʀʀᴏʀ ᴍᴇꜱꜱᴀɢᴇ ɪꜱ ɴᴏᴛ ʙᴇɪɴɢ ʟᴏɢɢᴇᴅ ʙʏ ᴜꜱ!"""
