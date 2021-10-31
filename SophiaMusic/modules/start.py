from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hi there,👋 {message.from_user.first_name}!
\nThis is Army Bot CREATED BY @projectking.
I play music on Telegram's Voice Chats.
\nFo More Help Use Buttons Below:
 """,
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MY OWNER", url="https://t.me/projectking")
                  ],[
                    InlineKeyboardButton(
                        "My group", url="https://t.me/Worldwide_friends_chatting_zonee")
                ],
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""*ARMY BOT IS ALIVE.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MY GROUP", url="https://t.me/Worldwide_friends_chatting_zonee")
                ]
            ]
        )
   )
