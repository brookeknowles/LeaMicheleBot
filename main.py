import os
from dotenv import load_dotenv
from discord.ext import commands

from functions import emojify, add_emoji, does_translation_exist, emojify_phrase

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
async def translateWord(ctx, *message):
    """ user types '!translateWord' followed by a message, bot then replies with that message translated to emojis
        message argument a tuple e.g. if they message "hello there", message = ("hello", "there")
    """

    output = emojify(message)[0]
    unknown = emojify(message)[1]

    await ctx.send(output)

    if len(unknown):    # list isn't empty, there were unknown words
        await ctx.send("Consider adding the unknown words to the dictionary with the !addWord command, in the format "
                       "name emoji \ne.g. '!addWord fire 🔥'")


@client.command()
async def translatePhrase(ctx, *, message):
    """ user types '!translatePhrase' followed by a phrase that cannot be translated exactly word by word,
        bot then replies with that phrase translated to emojis
        message argument a string
    """

    output = emojify_phrase(message)[0]
    unknown = emojify_phrase(message)[1]

    if unknown:
        await ctx.send("Consider adding the unknown phrase to the dictionary with the !addPhrase command, "
                       "in the format !addPhrase [phrase] emoji \ne.g. '!addPhrase [hello there] 👋'")
    else:
        await ctx.send(output)


@client.command()
async def addWord(ctx, *message):
    """ User can add an emoji and its english translation to the dictionary."""

    if len(message) != 2:
        await ctx.send("Incorrect format. Please try again in the format: !addWord name emoji \ne.g. '!addWord fire 🔥'")

    else:
        word = message[0]
        emoji = message[1]

        if not does_translation_exist(word):
            add_emoji(word, emoji)

            await ctx.send(word + " AKA " + emoji + " has been added to the dictionary!")
        else:
            stored_emoji = does_translation_exist(word)
            await ctx.send(word + " already exists in the dictionary as " + stored_emoji +
                           "\nIf you would like to update the translation, try the !updateWord command (e.g. "
                           "'!updateWord fire 🔥')")


@client.command()
async def addPhrase(ctx, *, message):
    """ should be in format !addPhrase [phrase] emoji e.g. '!addPhrase [brooke knowles] 😀'
        User can add an emoji and its english translation to the dictionary. """

    if '[' and "] " in message:
        phrase = message.split('[')[1].split(']')[0]
        emoji = message.split('] ')[1].split("\\\\")[0]

        if not does_translation_exist(phrase):
            add_emoji(phrase, emoji)

            await ctx.send(phrase + " AKA " + emoji + " has been added to the dictionary!")
        else:
            stored_emoji = does_translation_exist(phrase)
            await ctx.send(phrase + " already exists in the dictionary as " + stored_emoji +
                           "\nIf you would like to update the translation, try the !updatePhrase command (e.g. "
                           "'!updatePhrase [hello there] 👋')")
    else:
        await ctx.send("Incorrect format. Please try again in the format: !addPhrase [phrase] emoji "
                       "\ne.g. '!addPhrase [hello there] 👋'")


@client.command()
async def updateWord(ctx, *message):
    """ User can update a word's emoji translation. """

    if len(message) != 2:
        await ctx.send("Incorrect format. Please try again in the format: !updateWord name emoji \ne.g. "
                       "'!updateWord fire 🔥'")

    else:
        word = message[0]
        emoji = message[1]

        add_emoji(word, emoji)
        await ctx.send("The translation for " + word + " has been updated to " + emoji + "!")


@client.command()
async def updatePhrase(ctx, *, message):
    """ User can update a phrases' emoji translation.
        should be in format !updatePhrase [phrase] emoji e.g. '!updatePhrase [brooke knowles] 😀'
    """

    if '[' and "] " in message:
        phrase = message.split('[')[1].split(']')[0]
        emoji = message.split('] ')[1].split("\\\\")[0]

        add_emoji(phrase, emoji)
        await ctx.send("The translation for " + phrase + " has been updated to " + emoji + "!")

    else:
        await ctx.send("Incorrect format. Please try again in the format: !updatePhrase [phrase] emoji "
                       "\ne.g. !updatePhrase hello there 👋'")

client.run(TOKEN)
