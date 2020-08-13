import os
import discord
import random
import strings
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(strings.command_prefix):

        words = message.content.lower().split(' ')
        command = words[0][1:]

        if command == 'roll':
            response = roll(words)
            await message.channel.send(response)
            return
        else:
            await message.channel.send(strings.error % message.author.name)

def roll(words):
    if len(words) != 2:
        return strings.roll_error

    roll = words[1].split('d')

    if len(roll) != 2:
        return strings.roll_error

    try:
        dice = int(roll[1])
        count = int(roll[0])

        result = 0
        for i in range(count):
            result += random.randint(1, dice)
        return strings.roll_result % result
    except:
    	try:
    	    return strings.roll_result % random.randint(1, dice)
    	except:
            return strings.roll_error

client.run(TOKEN)
