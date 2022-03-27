import discord
from discord.ext import commands
import os, random, asyncio

#variables
token = "your bot token here"
dailyCat = yourMainChanelIdHere
dailyCatTest = yourChannelIdHere
cuteCats = "your main directory here"
cuteCatsTest = "your directory here"

#random file
random_filename = random.choice([
    x for x in os.listdir(cuteCatsTest)
    if os.path.isfile(os.path.join(cuteCatsTest, x))
])

client = commands.Bot(command_prefix = ":3 ")

#every day do this
async def send_daily():
    await client.wait_until_ready()
    channel = client.get_channel(dailyCatTest)
    while not client.is_closed():
        random_filename = random.choice([
            x for x in os.listdir(cuteCatsTest)
            if os.path.isfile(os.path.join(cuteCatsTest, x))
        ])
        previous = await channel.history().flatten()
        for i in range(len(previous) + 1):
            currentMessage = previous[i]
            if currentMessage.author.bot == True:
                attachment = currentMessage.attachments
                if attachment[0].filename == random_filename:
                    random_filename = random.choice([
                        x for x in os.listdir(cuteCatsTest)
                        if os.path.isfile(os.path.join(cuteCatsTest, x))
                    ])
                else:
                    break
            else:
                continue

        file = discord.File(cuteCatsTest+random_filename)
        fileRoot = cuteCatsTest+random_filename
        await channel.send(file=file, content="<@&your role id here> here is your cat")
        if os.path.exists(fileRoot):
            os.remove(fileRoot)
        else:
            print("the file has either already been deleted, or it broke, and the program can't read the file.")
        print('sent daily')
        await asyncio.sleep(10)

client.loop.create_task(send_daily()) #make it loop

client.run(token) #run the bot
