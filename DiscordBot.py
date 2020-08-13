import discord

token = ""

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("ti exoume?"):
        await message.channel.send("esu tha mas peis")
    if message.content.startswith("a kala"):
        await message.channel.send("panta kala")

client.run(token)
