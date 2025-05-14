"""from pyrogram import filters
from pyrogram.types import CallbackQuery
from helper.data import HACK_MODS, HACK_TEXT
from pyrogram import Client

@Client.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    await message.reply_text(
        HACK_TEXT,
        reply_markup=HACK_MODS
    )

@Client.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(_, query: CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(
        HACK_TEXT,
        reply_markup=HACK_MODS
    )
"""
