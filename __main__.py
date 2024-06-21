from discord.ext import commands, tasks
import discord
import systeminfo
import apikey
import time
import asyncio
import importantServices

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def periodic():
    await client.wait_until_ready()
    channel = client.get_channel(1253632767842062348)
    while True:
        await asyncio.sleep(1)
        f = open("trigger", "r")
        shouldTrigger = bool(f.readline())
        if shouldTrigger == True:
            status = f.readline()
            try:
                await channel.send(status)
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
    client.loop.create_task(periodic())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "status":
        await message.channel.send('CPU freq: ' + systeminfo.getCPUFreq() + '\nCPU usage: ' + systeminfo.getCPUUsage() + '\nRAM%: ' + systeminfo.getRAMUsage() + '\nUptime: ' + systeminfo.getUptime_Days())
        statuses = systeminfo.getStatus(importantServices.services())
        statusString = ''
        for status in statuses:
            statusString = statusString + "\n" + status
        await message.channel.send(statusString)
    if message.content == "bot status":
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

key = apikey.key()
client.run(key)