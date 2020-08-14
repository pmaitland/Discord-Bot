import os
import discord
import random
import re
import string
import strings
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

translator = str.maketrans('', '', string.punctuation)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.strip().lower()
    response = None

    if message.content.startswith(strings.command_prefix):
        content = message.content.split(' ')
        command = content[0][1:]
        if command == '8ball':
        	response = magicball(content)
        elif command == 'choose':
        	response = choose(content)
        elif command == 'help':
        	response = help(content)
        elif command == 'roll':
            response = roll(content)

    elif re.search(strings.reegex, message.content):
    	response = strings.ree
    elif message.content.translate(translator) == 'same':
    	response = strings.same

    if response:
        await message.channel.send(response)

def magicball(msg_content):
	if len(msg_content) > 1:
	    return strings.magicball_responses[random.randint(0, len(strings.magicball_responses) - 1)]
	else:
		return strings.magicball_error

def choose(msg_content):
    msg_content = msg_content[1:]
    options = ' '.join(msg_content).split(' or ')
    if len(options) > 1:
        return strings.choose_result % options[random.randint(0, len(options) - 1)]
    return strings.choose_nooptions

def help(msg_content):
	if len(msg_content) == 1:
		return strings.help_all

def roll(msg_content):
    if len(msg_content) != 2:
        return strings.roll_error

    roll = msg_content[1].split('d')

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
