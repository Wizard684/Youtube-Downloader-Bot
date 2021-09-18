from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url
    And Please Join For Watch Hindi Tv Serial  @HindiTvFlix"
    await message.reply_text(helptxt)
