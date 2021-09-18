from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🟣 Updation Channel 🟣", url="https://t.me/Mega_Bots_Updates")],
        [InlineKeyboardButton(
            "Report Bugs 🥰", url="https://t.me/Mega_Bots_Supporters")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nI Am Bot To Download YouTube Videos, But you must Join my Updation Channel 😊 /Help For More Info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
