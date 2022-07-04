import json

f = open('emojis.json')
data = json.load(f)


def emojify(message):
    """ Translates english text into emojis based off what each word's corresponding emoji is in
        the emojis.json file. """

    output = ""
    unknown_words = []

    for word in message:
        if word.lower() in data:
            emoji = data[word.lower()]
            output += emoji + ' '
        else:
            unknown_words.append(word)
            output += word + ' '

    return output, unknown_words


def add_emoji(name, emoji):
    """ Takes in an emoji and its name, and adds them to the list of emojis in emojis.json"""

    with open('emojis.json', "r") as info:
        # Read existing data into new variable and append to new data it
        emoji_data = json.load(info)
        emoji_data[name] = emoji

        # Write updated data stored in emoji_data variable to actual file
        with open('emojis.json', 'w') as f:
            json.dump(emoji_data, f, indent=4)

