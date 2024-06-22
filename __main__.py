from discord.ext import commands, tasks
import discord
import systeminfo
import apikey
import time
import asyncio
import importantServices
import threading
import errorWatch

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def periodic(channel):
    await client.wait_until_ready()
    sent = 0
    while True:
        await asyncio.sleep(1)
        f = open("trigger", "r")
        shouldTrigger = bool(f.readline())
        if shouldTrigger == True:
            status = f.readline()
            try:
                await channel.send(status)
                sent +=1
                open("trigger", "w").close()
            except TypeError:
                print('err')
        f.close()

@client.event
async def on_ready():
    channel = client.get_channel(1253632767842062348)
    await channel.send("connected")
    print(f'We have logged in as {client.user}')
    f = open("trigger", 'w')
    f.close()
    f = open("uptime", "w")
    f.write(str(time.time_ns()))
    f.close()
    client.loop.create_task(periodic(channel))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "status":
        await message.channel.send('CPU freq: ' + systeminfo.getCPUFreq() + '\nCPU usage: ' + systeminfo.getCPUUsage() + '\nRAM%: ' + systeminfo.getRAMUsage() + '\nUptime: ' + systeminfo.getUptime_Days())
        statuses = systeminfo.getStatus(importantServices.services())
        statusString = ''
        for status in statuses:
            statusString = statusString + "\n" + status
        await message.channel.send(statusString)

    if message.content.lower() == "bot status":
        f = open("uptime", "r")
        startTime = f.readline()
        f.close
        uptime = ((time.time_ns() - int(startTime))/60000000000)
        suffix = "minutes"
        if uptime > 60: 
            uptime = uptime / 60
            suffix = "hours"
        if uptime > 1440:
            uptime = uptime / 1440
            suffix = 'days'
        await message.channel.send('Bot has been up for: ' + str(uptime)+ " " + suffix)

watchdog = threading.Thread(target=errorWatch.watchdog)
watchdog.start()


key = apikey.key()
client.run(key)
