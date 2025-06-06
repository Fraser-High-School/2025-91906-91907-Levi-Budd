



import configparser

config = configparser.ConfigParser()

with open('settings.ini', 'w') as configfile:
    config['settings'] = {
        'difficulty': '4',
        'amount': '10',
        'mode': 'easy',
        'password': '1234'
    }
    config.write(configfile)


config.read('settings.ini')

difficulty = config['settings']['difficulty']
amount = config['settings']['amount']
mode = config['settings']['mode']
password = config['settings']['password']

print(f"Amount set to: {amount}")
print(f"Difficulty set to: {difficulty}")
print(f"Mode set to: {mode}")
print(f"Password set to: {password}")




        apple = StringVar()
        apple.set("apple")  # Set default value
        self.settings_optionmenu = OptionMenu(self.settings_frame,
                                            apple,
                                            "apple", "banana", "orange")
        self.settings_optionmenu.config(
                                        font=("arial", 14),
                                        bg=background_color,
                                        fg="#000000",
                                        )
        self.settings_optionmenu.grid(row=2, column=0, padx=5, pady=5)




        self.settings_optionmenu = OptionMenu(self.settings_frame,
                                            apple2,
                                            "apple", "banana", "orange")
        self.settings_optionmenu.config(
                                        font=("arial", 14),
                                        bg=background_color,
                                        fg="#000000",
                                        )
        self.settings_optionmenu.grid(row=2, column=1, padx=5, pady=5)


        self.settings_window = Toplevel(parent)
        self.settings_window.title("Settings")
        self.settings_window.geometry("360x425")
        self.settings_window.configure(bg=background_color)

        self.settings_frame = Frame(bg=background_color, master=self.settings_window)
        self.settings_frame.grid(sticky="n")
        self.settings_window.grid_rowconfigure(0, weight=1)
        self.settings_window.grid_columnconfigure(0, weight=1)