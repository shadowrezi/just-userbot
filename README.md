
## just-userbot
**is a Python userbot built using the Pyrogram library. It's designed to enhance your Telegram experience with various features and commands. With this userbot, you can perform actions like simulating typing, controlling your PC, make speech from text, encode and decode Qrcodes,  performing magic tricks, and even using ChatGPT for generating text.**


## 📖 Table of Contents
- [📦 Features](#-features)
- [📂 Userbot Structure](#-userbot-structure)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running userbot](#-running-userbot)
- [🤝 Contributing](#-contributing)


## 📦 Features

- **Prefixes are `/` and `.`**



- **All your message that starts with `/` will with typing effect, you need to try it :) ⌨️**

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

## 📂 Userbot Structure

```sh
└── just-userbot/
    ├── misc/
    │   ├── __init__.py 
    │   └── filters.py
    ├── plugins/
    │   ├── TextToSpeech.py
    │   ├── ai.py
    │   ├── arts.py
    │   ├── calculator.py
    │   ├── commands.py
    │   ├── count.py
    │   ├── exec.py
    │   ├── heart.py
    │   ├── jokes.py
    │   ├── music.py
    │   ├── nekobin.py
    │   ├── note.py
    │   ├── parsemode.py
    │   ├── pc_control.py
    │   ├── processing.py
    │   ├── qrcode.py
    │   ├── typing.py
    │   └── variables.py
    ├── data.json
    ├── requirements.txt
    └── userbot.py
```

## 🚀 Getting Started
### 🔧 Installation

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

9. Get your pexels api key:

   [Register and get api key](https://www.pexels.com/join-consumer/?onboarding=skipped)
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

   PEXELS_TOKEN=<your pexels api key>
   ```
### 🤖 Running userbot
   Windows:
      ```sh
      $ python userbot.py
      ```
   Linux:
      ```sh
      $ python3 usebot.py
      ```


## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/shadowrezi/userbot-template/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/shadowrezi/userbot-template/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/shadowrezi/userbot-template/issues)**: Submit bugs found or log feature requests for SHADOWREZI.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>
