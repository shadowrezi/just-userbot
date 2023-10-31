
## just-userbot
**is a Python userbot built using the Pyrogram library. It's designed to enhance your Telegram experience with various features and commands. With this userbot, you can perform actions like simulating typing, controlling your PC, make speech from text, encode and decode Qrcodes,  performing magic tricks, and even using ChatGPT for generating text.**


## Features

- **Prefixes are `/` and `.`**



- **All your message will with typing effect, you need to try it :) ⌨️**

- **.commands**: Get all commands

-  **.switch-typing**: Switch on/off typing

- **.music \<song name>**: Search and get any videos or songs from [Youtube 🎥](https://www.youtube.com/)

- **.gpt \<prompt>**: Utilize ChatGPT to generate text based on your prompt.

- **.shutdown**: Shutdown your PC with this command. No arguments required.

- **.restart**: Restart your PC using this command. No arguments needed.  🔄

- **.cancel**: Cancel any ongoing shutdown or restart process. No arguments required.

- **.magic**: Very beautiful effect with many hearts ❤️❤️❤️

- **.qrcode \<prompt>**: Create a qrcode

- **.decode** (replied on photo-message): Decode any qrcode

- **.gtts \<prompt>**: Make speech from text (language by default is ukrainian, plugins/TextToSpeech.py line 24) 

## Usage

**Start the bot in `just-userbot` folder only**

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/just-userbot.git
   ```
3. Goto bot folder:
   ```shell
   cd just-userbot
   ```
4. Create a virtual envorietment:
   
   Windows:
      ```shell
        $ python -m venv venv
      ```
   Linux:
      ```shell
         $ python3 -m venv venv
      ```
6. Activate venv:

   Windows:
      ```shell
      $ .\venv\Scripts\activate
      ```
   Linux:
      ```shell
      $ source venv/bin/activate
      ```
7. Install all requirements:
   ```shell
   $ pip install -r requirements.py
   ```
8. Get api id and api hash of your telegram account:

   [Official telegram's site for Developers](https://my.telegram.org/apps)

9. Get your openai api key:

   [Openai site: create or copy your key](https://platform.openai.com/account/api-keys)
4. Create a virtual envorietment:
   
   Windows:
      ```shell
        $ echo . > .env
      ```
   Linux:
      ```shell
         $ touch .env
      ```
11. Write in file `.env` this data:
   ```
   API_ID=<your api id>
   API_HASH=<your api hash>

   OPENAI_TOKEN=<your openai api key>
   ```

11. Start userbot:

   Windows:
      ```shell
      $ python userbot.py
      ```
   Linux:
      ```shell
      $ python3 usebot.py
      ```
