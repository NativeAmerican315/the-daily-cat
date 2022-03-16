import discord
from discord.ext import commands
import os, random, asyncio

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
        previous = await channel.history().flatten()
        for i in range(len(previous) + 1):
            currentMessage = previous[i]
            if currentMessage.author.bot == True:
                attachment = currentMessage.attachments
                if attachment[0].filename == random_filename:
                    random_filename = random.choice([
                        x for x in os.listdir(cuteCats)
                        if os.path.isfile(os.path.join(cuteCats, x))
                    ])
                else:
                    break
            else:
                continue
        file = discord.File(cuteCats+random_filename)
        await channel.send(file=file, content="<@&your role id here> here is your cat")
        if os.path.exists(file):
            os.remove(file)
        else:
            print("the file has either already been deleted, or it broke, and the program can't read the file.")
        print('sent daily')
        await asyncio.sleep(86400)

client.loop.create_task(send_daily()) #make it loop

client.run(token) #run the bot
