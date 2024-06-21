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
        usage = str(psutil.cpu_percent(.25))
        freq = str(psutil.cpu_freq()[0])
        memPercent = str(psutil.virtual_memory()[2])
        with open('/proc/uptime', 'r') as f:
            uptime = str(float(f.readline().split()[0])/86400)
        await message.channel.send('This is real data\n CPU freq: ' + freq + '\n CPU usage: ' + usage + '\n RAM%: ' + memPercent + '\n Uptime: ' + uptime)


key = apikey.key()
client.run(key)