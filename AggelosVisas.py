import discord

token = "NTM1OTkxMTgyMzIxMjU0NTE4.XEJ6sA.9JcLg4mkRKrBt7fdPfZ2WPDgung"

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("ti exoume?"):
        await message.channel.send("esu tha mas peis")
    if message.content.startswith("a kala"):
        await message.channel.send("panta kala")

client.run(token)