import discord
from discord.ext import commands
import os, random, asyncio, telegram_send

#variables
token = "your bot token here"
dailyCat = "your main channel id here"
dailyCatTest = "your test server channel id here"
cuteCats = "directory that holds all of the cat photos"

#random file
random_filename = random.choice([
    x for x in os.listdir(cuteCats)
    if os.path.isfile(os.path.join(cuteCats, x))
])

client = commands.Bot(command_prefix = ":3 ")

#every day do this
async def send_daily():
    await client.wait_until_ready()
    channel = client.get_channel(dailyCatTest)
    while not client.is_closed():
        random_filename = random.choice([
            x for x in os.listdir(cuteCats)
            if os.path.isfile(os.path.join(cuteCats, x))
        ])
        file = discord.File(cuteCats+random_filename)
        await channel.send(file=file, content="<@&your role id here> here is your cat")
        print('sent daily')
        telegram_send.send(messages=["Sent Daily"])
        await asyncio.sleep(86400)

client.loop.create_task(send_daily()) #make it loop

client.run(token) #run the bot
