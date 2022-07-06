import json


def reloadJSON():
    with open("emojis.json", "r") as f:
        return json.loads(f.read())


def add_to_JSON(data):
    with open('emojis.json', 'w') as f:
        return json.dump(data, f, indent=4)


def emojify(message):
    """ Translates english text into emojis based off what each word's corresponding emoji is in
        the emojis.json file. """

    output = ""
    unknown_words = []
    data = reloadJSON()

    for word in message:
        if word.lower() in data:
            emoji = data[word.lower()]
            output += emoji + ' '
        else:
            unknown_words.append(word)
            output += word + ' '

    return output, unknown_words


def emojify_phrase(message):
    data = reloadJSON()
    unknown = False

    if message.lower() in data:
        emoji = data[message.lower()]
        return emoji, unknown
    else:
        unknown = True
        return message, unknown


def add_emoji(word, emoji):
    """ Takes in an emoji and its corresponding word/phrase, and adds them to the list of emojis in emojis.json.
        If a translation for the word/phrase already exists, it updates the translation to the input emoji"""

    # Read existing data into new variable and append to new data it
    data = reloadJSON()
    data[word] = emoji

    # Write updated data stored in emoji_data variable to actual file
    add_to_JSON(data)


def does_translation_exist(word):
    """ Checks if a word/phrase exists in the emojis.json file. If it exists, function returns the corresponding emoji,
        otherwise will return False """

    data = reloadJSON()

    if word in data.keys():
        return data[word]
    else:
        return False
