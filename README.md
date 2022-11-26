# LeaMicheleBot

Fun little Discord bot that translates users messages from plain English into emojis, Lea Michele instagram style<sup>*</sup>

## Set Up on local machine

### Discord related set up
1. Head over to the [Discord Developer Portal](https://discord.com/developers/applications)
2.  Create a *new application* - [RealPython has a good tutorial on this](https://realpython.com/how-to-make-a-discord-bot-python/)
3.  Once you have created the application, note the token provided

### Application set up
1. Clone this repository
```shell
git clone https://github.com/brookeknowles/LeaMicheleBot.git
```
2. Open up the repository in your favourite IDE
3. Install the project dependencies:
```shell
pip3 install -r requirements.txt
```
4. Create a .env file with your token from the earlier step, the only line in the file should be:
```
TOKEN={your-bot-token}
```
5. Run the app:
```shell
python3 main.py
```

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
