



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


self.optionmenus_ref_dict['mode'].config(fg="#FF0000")


self.settings_label = Label(self.settings_frame,
                                text="These are the results of the 5 most \n"
                                    " recent quizzes out of X total\n"
                                    " quizzes, the lower the older.",
                                font=("arial", "14"),
                                justify="left",
                                wraplength=350,
                                bg=background_color,
                                )
        self.settings_label.grid(row=1, column=0, columnspan=2)
        self.settings_label.grid_rowconfigure(1, weight=1)
        self.settings_label.grid_columnconfigure(1, weight=1)
        
        for i in range(4):
            labels = ["Mode", "Name", "Save", "Results"]
            self.settings_options_labels = Label(self.settings_frame,
                                    text=labels[i],
                                    font=("arial", "14"),
                                    wraplength=350,
                                    bg=background_color,
                                    )
            self.settings_options_labels.grid(row=3, column=i, columnspan=1)
            self.settings_options_labels.grid_rowconfigure(1, weight=1)
            self.settings_options_labels.grid_columnconfigure(1, weight=1)

        # Create a frame to hold both OptionMenus
        self.optionmenu_frame = Frame(self.settings_frame, bg=background_color)
        self.optionmenu_frame.grid(row=4, column=0, columnspan=2, sticky="w")
        self.optionmenu_frame.grid_rowconfigure(1, weight=1)
        self.optionmenu_frame.grid_columnconfigure(1, weight=1)
        self.optionmenus_ref_dict = {}
        self.comboboxes_ref_dict = {}

        def create_optionmenus():
            optionmenus = [
            # this list contains all the data for the option menus
            # it goes: start text, options, row, collumn
            ["mode", "quiz", "math", 0, 0,],
            ["name", "yes", "no", 0, 1],
            ["save", "yes", "no", 0, 2],
            ["results", "yes", "no", 0, 3],

            ]

            for i in range(len(optionmenus)):
                default_state = StringVar()
                default_state.set(optionmenus[i][0])  # Set default value to the first option

                self.optionmenu = OptionMenu(self.optionmenu_frame, default_state, optionmenus[i][1], optionmenus[i][2])
                self.optionmenu.config(
                                        font=("arial", 12),
                                        bg=background_color,
                                        fg="#000000",
                                        highlightthickness=0,
                                        bd=1,
                                        width=6,
                                        relief="groove"
                )
                self.optionmenu["menu"].config(
                                        font=("arial", 12),
                                        bg=background_color,
                                        fg="#000000"
                                        
                )
                self.optionmenu.grid(row=optionmenus[i][3], column=optionmenus[i][4], padx=5, pady=5)
                self.optionmenu.grid_rowconfigure(1, weight=1)
                self.optionmenu.grid_columnconfigure(1, weight=1)

                self.optionmenus_ref_dict.update({optionmenus[i][0]: self.optionmenu})
        # frame to hold the comboboxes
        self.comboboxes_frame = Frame(self.settings_frame, bg=background_color)
        self.comboboxes_frame.grid(row=6, column=0, columnspan=2, sticky="w")
        self.comboboxes_frame.grid_rowconfigure(1, weight=1)
        self.comboboxes_frame.grid_columnconfigure(1, weight=1)

        def create_comboboxes():
            comboboxes = [
            # this list contains all the data for the combomenu
            # it goes: start text, options, row, collumn
            ["amount", "5", "10", "15", "20", 0, 0],
            ["length", "5", "10", "15", "20", 0, 1],
            ["password", "", "", "", "", 0, 2],
            ["backround color", "grey", "white", "black", "transparent", 0, 3],
            ]


            for i in range(len(comboboxes)):
                default_state = StringVar()
                default_state.set(comboboxes[i][0])  # Set default value to the first option

                self.comboboxes = Combobox(self.comboboxes_frame,
                                           values=[comboboxes[i][1], comboboxes[i][2], comboboxes[i][3], comboboxes[i][4]],
                                           font=("arial", 12),
                                           width=8,
                                           )
                self.comboboxes.grid(row=comboboxes[i][5], column=comboboxes[i][6], padx=5, pady=5)
                self.comboboxes.grid_rowconfigure(1, weight=1)
                self.comboboxes.grid_columnconfigure(1, weight=1)
                self.comboboxes.set(comboboxes[i][0])  # Set the default text to the first option

                self.comboboxes_ref_dict.update({comboboxes[i][0]: self.comboboxes})

        self.settings_button_frame = Frame(self.settings_frame,
                                    background=background_color)
        self.settings_button_frame.grid(sticky="ew", row=7)
        self.settings_button_frame.grid_rowconfigure(1, weight=1)
        self.settings_button_frame.grid_columnconfigure(1, weight=1)
        settings_button_details_list = [
        # text, color, command, row, column
        # put your buttons features in this list.
        ["Exit", "#f44336", lambda: print(), "0", "0"],
        ["Apply", "#aaaeff", lambda: print(), "0", "1"],
        ]
        self.button_ref_list = []
        #actually turns the variables into buttons
        for item in settings_button_details_list:
            self.make_button = Button(self.settings_button_frame,
                                text=item[0],
                                bg=item[1],
                                fg="#000000",
                                font=("Arial", "20", "bold"),
                                width=9,
                                command=item[2]
                                )
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.make_button.grid_rowconfigure(1, weight=1)
            self.make_button.grid_columnconfigure(1, weight=1)
                
        create_optionmenus()
        create_comboboxes()
        self.check_focus()  # Start checking focus

    def check_focus(self):
        focused_widget = self.settings_window.focus_get()
        for widget in list(self.comboboxes_ref_dict.values()) + list(self.optionmenus_ref_dict.values()):
            if focused_widget == widget:
                print(f"{widget} is focused")
                widget.set("")  # delete the text in the combobox
                break
        else:
            print("No combobox or optionmenu is focused")
        self.settings_window.after(200, self.check_focus)