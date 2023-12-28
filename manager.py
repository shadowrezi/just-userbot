from importlib import reload
from multiprocessing import Process

import customtkinter as ctk

import userbot


class BotControlApp:

    def __init__(self, master):
        ctk.set_default_color_theme('green')

        self.master = master
        self.master.title("Managing bot")
        # self.master.config(bg='#072a47')

        self.label = ctk.CTkLabel(master, text='Stopped')
        self.label.pack(pady=10)

        ctk.CTkButton(master, text='Start', command=self.start_bot).pack(pady=10)
        ctk.CTkButton(master, text='Stop', command=self.stop_bot).pack(pady=10)
        ctk.CTkButton(master, text='Restart', command=self.restart_bot).pack(pady=10)
        ctk.CTkButton(master, text='Quit', text_color='#ea0002', bg_color='#ffffff', command=self.quit_app).pack(pady=10)
        self.is_bot_runned = False
        self.bot = None

    def start_bot(self):
        if not self.is_bot_runned:
            self.is_bot_runned = True
            self.update_label()
            
            reload(userbot)
            self.bot = Process(
                target=userbot.main
            )
            self.bot.start()

    def stop_bot(self):
        if self.is_bot_runned:
            self.is_bot_runned = False
            self.update_label()

            self.bot.terminate()
            self.bot.join()

            print('Stopping bot!')

    def restart_bot(self):
        if self.is_bot_runned:
            self.stop_bot()
        self.start_bot()

    def update_label(self):
        self.label.configure(
            text='Started' if self.is_bot_runned else 'Stopped'
        )
    
    def quit_app(self):
        self.stop_bot()
        self.master.quit()


if __name__ == "__main__":
    root = ctk.CTk()
    app = BotControlApp(root)
    root.mainloop()
