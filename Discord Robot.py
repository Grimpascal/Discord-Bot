import discord

token = "isi dgn token bot mu"
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

client.run(token)