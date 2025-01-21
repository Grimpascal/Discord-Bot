import discord

intens = discord.Intents.all()
intens.message_content = True

client = client = discord.Client(intents=intens)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "Jumanji"))
    print('Bot sedang online broku')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hi'):
        await message.reply('haloooo', mention_author = True)

client.run("MTMzMDU5MzQ3Nzk4NTA0NjU5MA.Gz4Oaj.42_HQIewYE39J2NKZEtt-BoALBlSuDa8GLnLl8")