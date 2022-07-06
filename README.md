# LeaMicheleBot

Fun little Discord bot that translates users messages from plain English into emojis, Lea Michele instagram style<sup>*</sup>

## Set Up

I have this hosted on Heroku to mess around with on my servers with friends, but feel free to invite the bot to your server with [this link](https://discord.com/api/oauth2/authorize?client_id=991976546833289296&permissions=534723950656&scope=bot)

## Otherwise to run on local machine:

### Discord related set up
- Head over to the [Discord Developer Portal](https://discord.com/developers/applications)
- Create a *new application* - [RealPython has a good tutorial on this](https://realpython.com/how-to-make-a-discord-bot-python/)
- Once you have created the application, note the token provided

### Application set up
- Clone this repository
- Open up the repository in your favourite IDE
- Install the project dependencies:

  > pip3 install -r requirements.txt
- Create a .env file with the token:

  > TOKEN={your-bot-token}
- Run the app:

  > python3 main.py

## Using The Bot

| Command         | Example       |
| :------------- |:-------------|
| **!translateWord** lets the user translate a sentence, word by word | ![Screenshot](/screenshots/translate-word.png) |
| **!addWord** allows the user to add translations to words the bot does not know yet       | ![Screenshot](/screenshots/add-new-word.png)      |
| **!updateWord** allows the user to update the existing translation of a word to a different emoji    | ![Screenshot](/screenshots/update-word.png)      |
| **!translatePhrase** works similarly to the !translateWord command, but instead of translating the message word by word, the bot will translate the whole message as one phrase | ![Screenshot](/screenshots/translate-phrase.png) |
| **!addPhrase** allows the user to add translations for phrases the bot does not know yet       | ![Screenshot](/screenshots/add-new-phrase.png)      |
| **!updatePhrase** allows the user to update the existing translation of a phrase to different emojis    | ![Screenshot](/screenshots/update-phrase.png)|
| Custom emojis from Discord Nitro can also be used as translations    | ![Screenshot](/screenshots/custom-emoji.png)|

## Extra

<sup>*</sup>There is a hilarious (but totally fake) online conspiracy theory that Lea Michele, the actress and singer best known for her work on *Glee*, is illiterate and can only understand emoji's. [This website has a good rundown if you're interested](https://thetab.com/uk/2022/03/16/lea-michele-illiterate-conspiracy-243951)
