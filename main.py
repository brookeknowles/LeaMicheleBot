import os
from dotenv import load_dotenv
from discord.ext import commands

from functions import emojify, add_emoji

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')     # prints message log on terminal

    await client.process_commands(message)                          # need this so the commands don't get overwritten


@client.command()
async def translate(ctx, *message):
    """ user types '!translate' followed by a message, bot then replies with that message translated to emojis"""

    output = emojify(message)[0]
    unknown = emojify(message)[1]

    await ctx.send(output)

    if len(unknown):    # list isn't empty, there were unknown words
        await ctx.send("The following words do not currently have a translation: ")
        await ctx.send(unknown)
        await ctx.send("Consider adding them to the dictionary with the !add command, in the format {name} {emoji}" +
                       "\ne.g. '!add fire 🔥'")


@client.command()
async def add(ctx, *message):
    """ User can add an emoji and its english translation to the dictionary.
        At the moment the program needs to be terminated and then restarted for the bot to translate the added words"""

    if len(message) > 2:
        await ctx.send("Incorrect format. Please try again in the format: !add {name} {emoji} \ne.g. '!add fire 🔥'")

    else:
        name = message[0]
        emoji = message[1]

        add_emoji(name, emoji)

        await ctx.send("emoji has been added to the dictionary!")

client.run(TOKEN)
