# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from modules.config import PLAYLIST_IMG_URL, PRIVATE_BOT_MODE, adminlist
from modules.strings import get_string
from modules import YouTube, app
from modules.misc import SUDOERS
from modules.utils.database import (get_cmode, get_lang,
                                       get_playmode, get_playtype,
                                       is_active_chat,
                                       is_commanddelete_on,
                                       is_served_private_chat)
from modules.utils.database.memorydatabase import is_maintenance
from modules.utils.inline.playlist import botplaylist_markup


def PlayWrapper(command):
    async def wrapper(client, message):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "Bot is under maintenance. Please wait for some time..."
                )
        if PRIVATE_BOT_MODE == str(True):
            if not await is_served_private_chat(message.chat.id):
                await message.reply_text(
                    "**Private Music Bot**\n\nOnly for authorized chats from the owner. Ask my owner to allow your chat first."
                )
                return await app.leave_chat(message.chat.id)
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        audio_telegram = (
            (
                message.reply_to_message.audio
                or message.reply_to_message.voice
            )
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (
                message.reply_to_message.video
                or message.reply_to_message.document
            )
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if (
            audio_telegram is None
            and video_telegram is None
            and url is None
        ):
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_text("**🤖 𝐆𝐢𝐯𝐞 🙃 𝐒𝐨𝐦𝐞 💿 𝐐𝐮𝐞𝐫𝐲 😍\n💞 𝐓𝐨 🔊 𝐏𝐥𝐚𝐲 🥀 𝐒𝐨𝐧𝐠 🌷...**\n\n𝐔𝐬𝐚𝐠𝐞 : Lucky (Song Name) or /play (Song Name)",
                )
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="How to Fix this? ",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(
                _["general_4"], reply_markup=upl
            )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_18"])
            fplay = True
        else:
            fplay = None
        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper


# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
