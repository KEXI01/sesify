from pyrogram import filters
from pyrogram import Client
from helper.data import HACK_MODS,HACK_TEXT
from pyrogram.types import CallbackQuery
from src import app

 
@app.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    await message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


@app.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 
