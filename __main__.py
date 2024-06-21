import discord
import apikey
import psutil

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
        await message.channel.send("This is an example status\n The server is: Ok\n CPU usage: " + str(psutil.cpu_percent(.5)) + "\n Cpu Freq: " + str(psutil.cpu_freq()[0]))

key = apikey.key()
client.run(key)