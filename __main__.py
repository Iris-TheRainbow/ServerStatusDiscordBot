import discord
import apikey
import psutil
import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    global channel
    channel = client.get_channel('1253632767842062348')
    print(f'We have logged in as {client.user}')

@client.event
async def on_connect():
    f = open("uptime", "w")
    f.write(str(time.time_ns()))
    f.close()

    try:
        channel.send("Server Status Bot is back up")
    except:
        pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "status":
        usage = str(psutil.cpu_percent(.25))
        freq = str(psutil.cpu_freq()[0])
        memPercent = str(psutil.virtual_memory()[2])
        with open('/proc/uptime', 'r') as f:
            uptime = str(float(f.readline().split()[0])/86400)
        await message.channel.send('CPU freq: ' + freq + '\n CPU usage: ' + usage + '\n RAM%: ' + memPercent + '\n Uptime: ' + uptime)
    
    if message.content == "bot status":
        f = open("uptime", "r")
        startTime = f.readline()
        f.close
        uptime = ((time.time_ns() - int(startTime))/60000000000)
        suffix = "minutes"
        if uptime > 60: 
            uptime = uptime / 60
            suffix = "hours"
        elif uptime > 1440:
            uptime = uptime / 1440
            suffix = 'days'
        await message.channel.send('Bot has been up for: ' + str(uptime)+ " " + suffix)

key = apikey.key()
client.run(key)