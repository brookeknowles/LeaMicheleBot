import json

f = open('emojis.json')
data = json.load(f)


def emojify(message):
    """ Translates english text into emojis based off what each word's corresponding emoji is in
        the emojis.json file. """

    output = ""
    for word in message:
        if word.lower() in data:
            emoji = data[word.lower()]
            output += emoji + ' '
        else:
            print("not in dict")  # TODO change this, so it prompts user to add an emoji that fits with their word
            output += word

    return output
