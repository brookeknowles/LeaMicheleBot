import os
from dotenv import load_dotenv
from discord.ext import commands

from functions import emojify

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

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "general":
        if user_message.lower() == "hello bot" or user_message.lower() == "hi bot":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye bot":
            await message.channel.send(f'Bye {username}')
        await client.process_commands(message)      # need this so the commands don't get overwritten


@client.command()
async def translate(ctx, *message):
    output = emojify(message)
    await ctx.send(output)

client.run(TOKEN)
