import discord
import apikey

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Status":
        await message.channel.send("This is an example status\n The server is: Ok\n Uptime is: 37 days")

key = apikey.key()
client.run(key)