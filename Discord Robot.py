import discord

intens = discord.Intents.all()
intens.message_content = True

client = client = discord.Client(intents=intens)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "Orang Mancing"))
    print('Bot sedang online broku')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        return
    if message.channel.name == "welcome":
        if message.content.startswith('hi'):
            await message.reply('haloooo', mention_author = True)
    else:
        await message.reply('Not here')

client.run("")