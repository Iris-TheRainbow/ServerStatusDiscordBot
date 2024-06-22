from discord.ext import commands, tasks
import discord
import systeminfo
import apikey
import time
import asyncio
import importantServices
import threading
import errorWatch
import os

intents = discord.Intents.default()
intents.message_content = True
pingIris = '<@705965203807928381> '
if os.path.exists('disconnecttime'):
    os.remove('disconnecttime')

client = discord.Client(intents=intents)

async def periodic():
    await client.wait_until_ready()
    global sent
    sent = 0
    while True:
        await asyncio.sleep(1)
        if sent < 3:
            f = open("trigger", "r")
            shouldTrigger = bool(f.readline())
            if shouldTrigger == True:
                status = f.readline()
                try:
                    await channel.send('<@705965203807928381> ' + status)
                    sent +=1
                    open("trigger", "w").close()
                except TypeError:
                    print('err')
            f.close()

@client.event
async def on_ready():
    global channel
    channel = client.get_channel(1253632767842062348)
    await channel.send("connected")
    print(f'We have logged in as {client.user}')
    f = open("trigger", 'w')
    f.close()
    f = open("uptime", "w")
    f.write(str(time.time_ns()))
    f.close()
    client.loop.create_task(periodic())
    if os.path.exists('disconnecttime'):
        with open('disconnecttime') as f:
            downtime = f.readline()
            downtime = ((time.time_ns() - int(downtime))/60000000000)
            suffix = " minutes"
            if downtime > 60: 
                downtime = downtime / 60
                suffix = " hours"
            if downtime > 1440:
                downtime = downtime / 1440
                suffix = ' days'
            downtime = round(downtime, 1)
            await channel.send(pingIris + 'your server was disconnected for ' + str(downtime) + suffix)
            os.remove('disconnecttime')            

@client.event
async def on_disconnect():
    print('logged downtime')
    if not os.path.exists('disconnecttime'):
        with open('disconnecttime', 'w') as f:
            f.write(str(time.time_ns()))
            f.close()

@client.event
async def on_shard_resumed():
    if os.path.exists('disconnecttime'):
        with open('disconnecttime') as f:
            downtime = f.readline()
            downtime = ((time.time_ns() - int(downtime))/60000000000)
            suffix = " minutes"
            if downtime > 60: 
                downtime = downtime / 60
                suffix = " hours"
            if downtime > 1440:
                downtime = downtime / 1440
                suffix = ' days'
            downtime = round(downtime, 1)
            await channel.send(pingIris + 'your server was disconnected for ' + str(downtime) + suffix)
            os.remove('disconnecttime') 

@client.event
async def on_resumed():
    if os.path.exists('disconnecttime'):
        with open('disconnecttime') as f:
            downtime = f.readline()
            downtime = ((time.time_ns() - int(downtime))/60000000000)
            suffix = " minutes"
            if downtime > 60: 
                downtime = downtime / 60
                suffix = " hours"
            if downtime > 1440:
                downtime = downtime / 1440
                suffix = ' days'

            await channel.send(pingIris + 'your server was disconnected for ' + str(downtime) + suffix)
            os.remove('disconnecttime') 

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
        uptime = round(uptime, 1)
        await message.channel.send('Bot has been up for: ' + str(uptime)+ " " + suffix)

watchdog = threading.Thread(target=errorWatch.watchdog)
watchdog.start()


key = apikey.key()
client.run(key)
