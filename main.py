#imports
import discord
from discord.ext import commands
import os, random, asyncio

#variables
token = "your bot token here" #to control the bot
dailyCat = "your main channel id here" #the main channel the bot should post to 
dailyCatTest = "your test server channel id here" #the test channel
cuteCats = "directory that holds all of the cat photos" #all of the cats

#gets a random file
random_filename = random.choice([
    #for every cat
    x for x in os.listdir(cuteCats)
    #get the file and set it to the variable
    if os.path.isfile(os.path.join(cuteCats, x))
])

#makes the bot
client = commands.Bot(command_prefix = ":3 ")

#the actual function
async def send_daily():
    await client.wait_until_ready() #waits until the client is done setting up
    channel = client.get_channel(dailyCat) #gets the main channel
    while not client.is_closed(): #when the bot is up and running
        random_filename = random.choice([ #make a new file choice
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
        file = discord.File(cuteCats+random_filename) #get the file
        await channel.send(file=file, content="<@&your role id here> here is your cat") #and print the message
        print('sent daily') #make a note to the bot that it sent the daily
        await asyncio.sleep(86400) #wait 24 hours

client.loop.create_task(send_daily()) #loop the function
client.run(token) #and run the bot.
