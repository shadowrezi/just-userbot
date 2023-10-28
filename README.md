
## just-userbot
is a Python userbot built using the Pyrogram library. It's designed to enhance your Telegram experience with various features and commands. With just-userbot, you can perform actions like simulating typing, controlling your PC, performing magic tricks, and even using ChatGPT for generating text.


## Features

- **All your message will with typing effect, you need to try it :) ⌨️**

- **.commands**: Get all commands

-  **.switch-typing**: Switch on/off typing

- **.music \<song name>**: Search and get any videos or songs from [Youtube 🎥](www.youtube.com/)

- **.gpt \<prompt>**: Utilize ChatGPT to generate text based on your prompt.

- **.shutdown**: Shutdown your PC with this command. No arguments required.

- **.restart**: Restart your PC using this command. No arguments needed.  🔄

- **.cancel**: Cancel any ongoing shutdown or restart process. No arguments required.

- **.magic**: Very beautiful effect with many hearts ❤️❤️❤️

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
   ```shell
   python -m venv venv
   ```
5. Activate venv:

   Windows:
      ```shell
      .\venv\Scripts\activate
      ```
   Linux:
      ```shell
      source venv/bin/activate
      ```
6. Install all requirements:
   ```shell
   pip install -r requirements.py
   ```
7. Get api id and api hash of your telegram account:

   [Official telegram's site for Developers](https://my.telegram.org/apps)

8. Get your openai api key:

   [Openai site: create or copy your key](https://platform.openai.com/account/api-keys)

<!-- 9. Create `.env` file:

   Windows (remove '1' from file):
      ```shell
      echo 1 > .env
      ```
      
   Linux:
      ```shell
      touch .env
      ``` -->
9. Write in file `.env` this data:
   ```
   API_ID=<your api id>
   API_HASH=<your api hash>

   OPENAI_TOKEN=<your openai api key>
   ```

10. Start userbot:
   ```shell
   python userbot.py
   ```
11. Try all commands:
   ```
   .commands (get all commands)
   .switch-typing (switch on/off typing)
   .magic
   .gpt <prompt>
   .shutdown  (shutdown pc, Linux and Windows)
   .restart  (restart pc, Linux and Windows)
   .cancel  (cancel restart or pc, Linux and Windows)
   .music <prompt>
   ```
