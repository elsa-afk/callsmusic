from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Haii guys!, {message.from_user.first_name}!</b>
Aku adalah bot music voice chat group!
Aku Akan Menemanimu Dengan Alunan Musik!.
Apabila Kurang Mengerti,Bisa Pc Ownerku Yakk!.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Owner Aku!", url="https://t.me/afterdaytoxic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Instagram Aku!", url="https://www.instagram.com/ronaldysyach_/"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Cara Menggunakan Aku!", url="https://telegra.ph/Tasya-03-22"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "Hai, apakah anda ingin memainkan sebuah lagu?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="Close"
                    )
                ]
            ]
        )
    )
