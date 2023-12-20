# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import Client, filters

from modules import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/33c79a7b5a5eed8f87d2d.jpg",
        caption=f"""🥀 𝐍𝐨𝐰 𝐌𝐲 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐈𝐬 𝐏𝐮𝐛𝐥𝐢𝐜 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐑𝐞𝐩𝐨 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐌𝐲 𝐂𝐨𝐝𝐞 ♕, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 𝐒𝐮𝐛𝐜𝐫𝐢𝐛𝐞 𝐎𝐮𝐫 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥  :
  [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://youtube.com/@HIPOGESTUDYHUB)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐑𝐞𝐩𝐨 🥀", url=f"https://github.com/ITS-LUCKY-BOY")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 🥀", url=f"https://t.me/DX_LUCKY_143")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/WorldFriends_143"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/DX_INFO")
                ]
            ]
        ),
    ) 

# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
