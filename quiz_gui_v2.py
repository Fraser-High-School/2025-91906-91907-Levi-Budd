# importing tkinter, time, 
# and questions & answers from questions.py
from tkinter import *
from tkinter.ttk import Combobox
from time import time, strftime, localtime
import time
import questions as q
# os is imported to open the results file
import os
# configparser is imported to read the config file
import configparser
# i set these variables here so that they can be used in questions.py



class Quiz():
    
    """
    this tool is used to quiz people using the questions and answers set by the operator,
    it takes the questions and answers from 'questions.py'
    """
    def __init__(self, root):
        # this grabs all the settings from the settings.ini file
        self.error_message = ""
        try:
            config = configparser.ConfigParser()
            config.read('settings.ini')
            self.mode = str(config['settings']['mode'])
            self.amount = int(config['settings']['amount'])
            self.difficulty = int(config['settings']['difficulty'])
            self.password = str(config['settings']['password'])
            self.do_name = config.getboolean('settings', 'name')
            self.do_save = config.getboolean('settings', 'save')
            self.do_results = config.getboolean('settings', 'results')
            self.color = str(config['settings']['color'])
        except (ValueError, KeyError) as e:
            # if there is an error, it will set the mode to quiz, amount to 5, difficulty to 5, name to True, save to True, results to True, and color to grey.
            self.error_message = ("Error reading settings.ini:\n" + str(e))
            config = configparser.ConfigParser()
            config.read('settings.ini')
            #put stff here
            self.mode = "quiz"
            self.amount = 5
            self.difficulty = 2
            self.password = str(config['settings']['password'])
            self.do_name = True
            self.do_save = True
            self.do_results = True
            self.color = "grey"
        # this sets the mode to quiz or math.
        if self.mode == "quiz":
            self.answers = q.Answers
            self.questions = q.Questions
        elif self.mode == "math":
            q.gen_questions()
            self.answers = q.Math_Answers
            self.questions = q.Math_Questions
        # global variable for background color, so it can be used in other classes.
        global background_color
        # if the color is grey, it will set the background color to a nicer shade of grey.
        if self.color == "grey":
            background_color = "#b3b3b3"
        else:
            # if the color is not grey, it will set the background color to the color specified in the settings.ini file.
            background_color = self.color

        # results will hold all the data, this includes time taken, date, questions answered, and correct answers.
        self.results = []
        # these track time and date.
        self.start_time = 0.0
        self.start_date = ""
        # these variables are used to keep track of the variables to write to results.txt.
        # they have to be set outside of the function so they arent reset every time the function is called.
        self.counter = 0
        self.length = len(self.questions)
        self.correct = 0
        self.incorrect = 0
        self.early_finish = False
        self.name = ""
        # these are to tell the program if the name has been said or not, and if it is done.
        self.name_said = False
        self.name_done = False
        # change answer_length to change the max length of the answer
        # this also affects max name length.
        self.answer_length = 30



        
        # sets the size of the window and its color
        root.geometry("360x300")
        try:
            root.configure(bg=background_color)
        except Exception:
            # if there is an error, it will set the background color to grey.
            background_color = "#b3b3b3"
            root.configure(bg=background_color)
            self.color = "error"

        # the frame holding the entire gui is created here
        self.quiz_frame = Frame(padx=10, pady=10, bg=background_color)
        self.quiz_frame.grid()

        
        # the heading is made here
        self.quiz_heading = Label(self.quiz_frame,
                                  text="Quiz Program",
                                  font=("arial", "25"),
                                  bg=background_color,
                                  )
        self.quiz_heading.grid(row=0)
        
        # the entrybox where you put in your answer is here
        self.quiz_entry = Entry(self.quiz_frame,
                                  font=("Arial", "26"),
                                  width=(12),
                                  )
        self.quiz_entry.grid(row=2, padx=1, pady=1)

        # is an label which tells the use where to place the answer
        self.quiz_entry_instructions_color = Label(self.quiz_frame,
                                  text="Please enter your answer above",
                                  font=("arial", "12"),
                                  fg="#FFFF00",
                                  bg=background_color,
                                  )
        self.quiz_entry_instructions_color.grid(row=3, padx=1, pady=1,)
        # tell the use the color errored
        if self.color == "error" and self.error_message == "":
             self.quiz_entry_instructions_color.config(text="Color setting invalid, defaulting to grey.", fg="#FF0000")
        elif self.color == "white" or self.color == "#FFFFFF":
            background_color = self.color
            self.quiz_entry_instructions_color.config(fg="#000000")
        if self.error_message != "":
            # if there is an error message, it will display it in the entry box instructions color label.
            self.quiz_entry_instructions_color.config(text=self.error_message, fg="#FF0000")
            # and set the background color to grey.
            background_color = "#b3b3b3"
            root.configure(bg=background_color)
        

        # another label that explains how to start quiz
        question = "Press start quiz to start answering questions!"
        self.quiz_instructions = Label(self.quiz_frame,
                                  text=question,
                                  font=("arial", "22"),
                                  wraplength=350, width=20, height=3,
                                  bg=background_color,
                                  )
        self.quiz_instructions.grid(row=4)

        # makes the frame all the buttons are stored in
        self.button_frame = Frame(self.quiz_frame,
                                bg=background_color,)
        self.button_frame.grid(sticky="ew")

        

        # These two functions start the buttons up, case is set as default to make
        # the base buttons.
        self.buttonswitch_left("default")
        self.buttonswitch_right("default")
        

    # this functions creates the right button, and switches it to the next button depending on the
    # variables in the list.
    def buttonswitch_right(self, case):
        button_details_list = [
            # text, color, command, row, column
            # put your buttons features in list.
            ["results", "#aaaeff", lambda: self.open_results(), "normal"],
            ["finish", "#ffe600", lambda: [setattr(self, "early_finish", True), self.buttonswitch_left("end"), self.open_results()], "normal"],
        ]
        self.right_button_ref_list = []

        # this else if statement tells the function which button to create depending on the case variable.
        if case == "default":
                state = 0
        elif case == "finish":
                state = 1
                root.unbind('<Return>')
        # this statement creates the button depending on the state variable.
        self.make_button = Button(self.button_frame,
                                text=button_details_list[state][0],
                                bg=button_details_list[state][1],
                                fg="#000000",
                                font=("Arial", "20", "bold"),
                                width=9,
                                state=button_details_list[state][3],
                                command=button_details_list[state][2]
                                )
        self.make_button.grid(padx=3, row=0, column=1)
        self.right_button_ref_list.append(self.make_button)
    
          
    # this functions creates the left button, and switches it to the next button depending on the
    # variables in the list.
    def buttonswitch_left(self, case):
        button_details_list = [
            # text, color, command, row, column
            # put your buttons features in list.
            ["Start Quiz", "#00ff08", lambda: [self.buttonswitch_left("begin"), self.question_answer()], "normal"],
            ["Submit", "#00ff08", lambda:self.question_answer(), "normal"],
            ["Submit", "#00ff08", lambda:print("how did you press this??"), "disabled"],
        ]
        self.left_button_ref_list = []

        # this else if statement tells the function which button to create depending on the case variable.
        if case == "default":
                state = 0
        elif case == "begin":
                self.buttonswitch_right("finish")
                state = 1
                # when the quiz is started, start_time is set to the current time.
                self.start_time = time.time()
                # grab the current time and date for the end of the quiz.
                self.start_date = strftime("%Y-%m-%d %H:%M:%S", localtime())
                
                
        elif case == "end":
                self.buttonswitch_right("default")
                state = 2
                
                self.write_to_file(self. results)
                # i unbind the enter key so you cant keep calling the function after the quiz is finished.
                root.unbind('<Return>')
                # disable the entry box so you cant enter anything after the quiz is finished.
                self.quiz_entry.config(state=DISABLED)
        
        # this statement creates the button depending on the state variable.
        self.make_button = Button(self.button_frame,
                                text=button_details_list[state][0],
                                bg=button_details_list[state][1],
                                fg="#000000",
                                font=("Arial", "20", "bold"),
                                width=9,
                                state=button_details_list[state][3],
                                command=button_details_list[state][2]
                                )
        self.make_button.grid(padx=3, row=0, column=0)

        self.left_button_ref_list.append(self.make_button)


    # this function makes the results window
    def open_results(self):
        if self.do_results:
            Results_window = ResultsWindow(root)

    def open_settings(self):
        Settings_window = SettingsWindow(root)


    def blank_checker(self):
        """
        This function checks if the text is not blank, and returns True if it is not blank.
        """
        blank_checker = bool(self.quiz_entry.get().strip())
        if blank_checker == True:
             self.quiz_entry_instructions_color.config(text="this cannot be blank.", fg="#FF0000")
        return blank_checker
        
                


    

    def question_answer(self):
            
            #this checks if the counter (amount of questions answered) is less than the length of the question list.
            # if it is, it will show the next question and continue the quiz,
            # otherwise it will disable the submit button and end the quiz.
            data_list = []
            if self.counter == 0 and self.quiz_entry.get() == self.password:
                self.open_settings()
                return
            # if the entry box is blank, and its not the first go it will end the function and tell you it cant be blank
            if not self.blank_checker() and self.counter > 0:
                        self.quiz_entry_instructions_color.config(text="this cannot be blank.", fg="#FF0000")
                        return
            
            if self.blank_checker() and self.counter > 0 and self.mode == "math":
                
                # if the mode is 2, it will check if the answer is a number, and if it is not, it will end the function and tell you it must be a number.
                try:
                    int(self.quiz_entry.get())
                except ValueError:
                    self.quiz_entry_instructions_color.config(text="this must be a number.", fg="#FF0000")
                    return


            if self.counter == 0 and self.do_name:
                self.quiz_instructions.config(text="Please submit your name.")
                # i bind the enter key so that you can press enter to submit your answer.
                root.bind('<Return>', lambda event: self.question_answer())

                if self.name_said == True:
                    # if name is blank it ends the function and tells the user to enter a name.
                    if not self.blank_checker():
                        self.quiz_entry_instructions_color.config(text="this cannot be blank.", fg="#FF0000")
                        return
                    
                    # this is where the name is set, it is set to the entry box.
                    self.name = self.quiz_entry.get()
                    self.name = self.name[0:self.answer_length]
                    self.quiz_entry.delete(0, END)
                    self.quiz_entry_instructions_color.config(text="Please enter your answer above", fg="#FFFF00")
                    self.quiz_instructions.config(text="Press start quiz to start answering questions!")
                    self.name_done = True
                self.name_said = True


            if self.name_done == True or self.do_name == False:
                if self.name_done == False:
                     self.name = "disabled"
                     root.bind('<Return>', lambda event: self.question_answer())
                
                if self.counter < self.length:
                    # Bind Enter key to submit the answer.
                    # i do this here so that it only binds when the quiz is actually started.
                    if self.counter == 0:
                        self.start_taken_time = time.time()
                    

                    question = self.questions[self.counter]
                    self.quiz_instructions.config(text=question, fg="#9C0000")
                
                if self.counter > 0:

                    
                    # counter_less_1 is used because lists start at 0, not 1.
                    counter_less_1 = self.counter - 1
                    
                    # block below sets answer to lowercase, remove leading and trailing spaces, and limit to first 30 characters.
                    answer = self.quiz_entry.get().strip().lower()
                    answer = answer[0:self.answer_length]
                    self.quiz_entry_instructions_color.config(text="Please enter your answer above", fg="#FFFF00")

                    # appends the question number, question text, and answer to the data_list.
                    data_list.append([self.counter, self.questions[counter_less_1], answer])
                    # this clears the entry box so you can enter the next answer, gets the correct answer.
                    self.quiz_entry.delete(0, END)
                    if self.mode == 2:
                         correct_answer = self.answers[counter_less_1]
                    else:
                         correct_answer = self.answers[counter_less_1]
                    

                    # this block gets the time taken for the question, and appends it to the data_list.
                    end_taken_time = time.time()

                    # this just changes the text depending on if the answer is correct or not.
                    # it also appends the correctness to the data_list.
                    if answer in correct_answer:
                        self.quiz_entry_instructions_color.config(text="Correct!", fg="#00ff08")
                        data_list.append(["correct"])
                        self.correct += 1
                    else:
                        self.quiz_entry_instructions_color.config(text="Incorrect!", fg="#ff0000")
                        data_list.append(["incorrect"])
                        self.incorrect += 1

                    # math getting the time taken for the question.
                    elapsed_time = end_taken_time - self.start_taken_time
                    minutes = int(elapsed_time // 60)
                    seconds = round(elapsed_time % 60, 2)

                    # this appends the time taken to the data_list.
                    data_list.append([minutes, seconds])
                    data_list = sum(data_list, [])
                    self.results.append(data_list)
                    self.start_taken_time = time.time()
                    # convenient for debugging, lets me see if the data_list is being created correctly.
                    print(data_list)

                # increment counter by 1 to move to the next question
                self.counter += 1

                # ends quiz if counter is greater than length of question list.
                if self.counter > self.length:
                    self.buttonswitch_left("end")
                    # may remove self.openresults() here. idk
                    self.open_results()
                    self.quiz_entry.config(state=DISABLED)
                    if self.do_results:
                        self.quiz_entry_instructions_color.config(text="Quiz Finished! go to results page for results!", fg="#00FFFF")
                    elif not self.do_results:
                        self.quiz_entry_instructions_color.config(text="Quiz Finished! Talk to your operator!", fg="#00FFFF")


                  
                    



    # this function writes everything to the results.txt file
    
    def write_to_file(self, data):
        if self.do_save == False:
            return
        with open("results.txt", "a") as r:
            # Loop through the data to write each question's details
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            elapsed_minutes = int(elapsed_time // 60)
            elapsed_seconds = round(elapsed_time % 60, 2)
            date = self.start_date
            

            
            # write the start of the results file, including the name, date, and questions answered.
            r.write(f"""
-------------------------------------------TEST RESULTS----------------------------------------------------------
Name: {self.name}
Test started: {date}
Questions correct: {self.correct}/{self.length}
The formatting is as follows:
Question Number : Question Text : Given Answer : Correct or Wrong : minutes : seconds
""")        
            # this loops through the data to write each question's details
            
            for tracker in range(len(data)):
                question_number = data[tracker][0]  # Question number (start from 0)
                question_text = data[tracker][1]  # Question text
                given_answer = data[tracker][2]  # Given answer
                correctness = data[tracker][3]  # "incorrect" or "correct" based on logic
                minutes = data[tracker][4]  # Elapsed time in minutes per question
                seconds = data[tracker][5]  # Elapsed time in seconds per question

                # Write the formatted data to the results file
                r.write(f"""
{question_number} : {question_text} : {given_answer} : {correctness} : {minutes} : {seconds}
""")        
                
            # check if the quiz was finished early, and sets early_finish_text to the string if it was.
            early_finish_text = ""
            if self.early_finish == True:
                 early_finish_text = "Quiz was finished early."
            r.write(f"""

Test Finished in: {elapsed_minutes} minutes and {elapsed_seconds} seconds.
{early_finish_text}

""")
            # this block writes the summary results to summary_results.txt.
            
            with open("summary_results.txt", "a") as r:
 
                sum_date = strftime("%m-%d", localtime())
                r.write(f"""{sum_date}: {self.correct}/{self.length} Questions Correct.\n""")
                
            

class ResultsWindow():
    """
    This class creates the results window, which shows the results of the quiz.
    """

    def __init__(self, parent):
        """
        This function creates the results window, which shows the results of the quiz.
        """




        # setting results window size, color, title, and as a Toplevel window.
        self.results_window = Toplevel(parent)
        self.results_window.title("Results")
        self.results_window.geometry("360x425")
        self.results_window.configure(bg=background_color)

        # making the frame that holds all the widgets, and making its master the results window itself.
        self.results_frame = Frame(bg=background_color, master=self.results_window)
        self.results_frame.grid(sticky="n")

        # this is to make the frame expand to fill the window, and to make it scrollable if needed.
        self.results_window.grid_rowconfigure(0, weight=1)
        self.results_window.grid_columnconfigure(0, weight=1)
        
        # this is creating the heading
        self.results_heading = Label(self.results_frame,
                                text="Results",
                                font=("arial", "25"),
                                
                                bg=background_color,
                                )            
        self.results_heading.grid(row=0, column=0, sticky="n")

        # this is creating the label that explains what the results are
        self.results_label = Label(self.results_frame,
                                text="These are the results of the 5 most \n"
                                    " recent quizzes out of X total\n"
                                    " quizzes, the lower the older.",
                                font=("arial", "14"),
                                justify="left",
                                wraplength=350,
                                bg=background_color,
                                )
        self.results_label.grid(row=1, column=0)

        # this is creating the listbox that holds the summarized results
        self.results_list = Listbox(self.results_frame,
                                font=("Arial", "14"),
                                width=27,
                                height=5,
                                bg='lime',
                                )
        self.results_list.grid(row=2, column=0, padx=1, pady=1)
        
        # Define a method to show results
        def show_results():
            with open("summary_results.txt", "r") as r:
                lines = r.readlines()  # Read all lines from the file
                for i in range(min(5, len(lines))):  # Check the last 5 lines
                    line = lines[-(i + 1)].strip()  # Access lines from the bottom up
                    self.results_list.insert(END, line)  # Insert the line into the results_list
                    if i >= 4:
                         self.results_list.config(bg='#f6edab')
                         
        # Call the function to insert the result
        show_results()

        def restart_quiz():
            # Destroy all widgets in the root window to reset the GUI
            for widget in root.winfo_children():
                widget.destroy()
            # Reinitialize the quiz GUI
            Quiz(root)

        # further explanation of the results window, tells user what the buttons do, and what the color of the listbox means.
        self.results_info = Label(self.results_frame,
                                text="You can see more in-depth results (what \n" \
                                "questions were wrong specifically) by \n" \
                                "going to the file. If the box is yellow, then \n" \
                                "there are more results in the file than shown here.",                                       
                                font=("arial", "14"),
                                justify="left",
                                wraplength=350,
                                bg=background_color,
                                )
        self.results_info.grid(row=3, column=0)

        # this is creating the frame that holds the buttons
        self.results_button_frame = Frame(self.results_frame,
                                    background=background_color)
        self.results_button_frame.grid(sticky="ew", row=4)

        # list to hold the button features to be created below.
        results_button_details_list = [
        # text, color, command, row, column
        # put your buttons features in this list.
        ["Restart", "#f44336", lambda: restart_quiz(), "0", "0"],
        ["To File", "#aaaeff", lambda: os.startfile("results.txt"), "0", "1"],
        ]
        self.button_ref_list = []
        #actually turns the variables into buttons
        for item in results_button_details_list:
            self.make_button = Button(self.results_button_frame,
                                text=item[0],
                                bg=item[1],
                                fg="#000000",
                                font=("Arial", "20", "bold"),
                                width=9,
                                command=item[2]
                                )
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

class SettingsWindow():
    """
    This class creates the settings window, which allows the user to change their settings in a GUI.

    In this window i used the pack geometry manager instead of grid, this is because was having tons of
    issues with grid using the combo and menuboxes, and didnt see a reason to spend more time on finding out why grid wasn't working.
    """

    def __init__(self, parent):
        # this grabs all the settings from the settings.ini file
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.config_list = [
            config['settings']['mode'],
            config['settings']['name'],
            config['settings']['save'],
            config['settings']['results'],
            config['settings']['amount'],
            config['settings']['difficulty'],
            config['settings']['password'],
            config['settings']['color']
        ]

        # setting settings window size, color, title, and as a Toplevel window.
        self.settings_window = Toplevel(parent)
        self.settings_window.title("Settings")
        self.settings_window.geometry("460x410")
        self.settings_window.configure(bg=background_color)

        # making the frame that holds all the widgets, and making its master the settings window itself.
        self.settings_frame = Frame(bg=background_color, master=self.settings_window)
        self.settings_frame.pack(fill="both", expand=True)

        # simple function to restart the quiz, same as in ResultsWindow.
        def restart_quiz():
            # Destroy all widgets in the root window to reset the GUI
            for widget in root.winfo_children():
                widget.destroy()
            # Reinitialize the quiz GUI
            Quiz(root)

        # this is creating the heading
        self.settings_heading = Label(self.settings_frame,
                                text="Settings",
                                font=("arial", "25"),
                                bg=background_color,
                                )            
        self.settings_heading.pack(pady=(5, 0))

        # this is creating the label says how to use the settings window
        self.settings_label = Label(self.settings_frame,
                                text="This is the settings window, you can change several settings down below.",
                                font=("arial", "14"),
                                justify="left",
                                wraplength=350,
                                bg=background_color,
                                )
        self.settings_label.pack(pady=(0, 10))

        # this is a ref list for the labels, so we can change them later if needed.
        self.settings_label_ref_list = []

        # this function creates the labels for the optionmenus and comboboxes, it is called twice, once for each type.
        def create_labels(type):
            # frame to hold the labels, this is so they can be aligned in a row and so the backround color can be set.
            label_row_frame = Frame(self.settings_frame, bg=background_color)
            label_row_frame.pack(fill="x")

            # if statement to determine which type of labels to create
            if type == "optionmenus":
                labels = ["Mode", "Name", "Save", "Results"]

            elif type == "comboboxes":
                labels = ["Amount", "Length", "Password", "Color"]

            # for loop to create the labels, it goes through the list of labels and creates a label for each item in the list.
            for i in range(len(labels)):
                self.settings_options_labels = Label(label_row_frame,
                                        text=labels[i],
                                        font=("arial", "14"),
                                        wraplength=350,
                                        bg=background_color,
                                        anchor="center"
                                        )
                self.settings_options_labels.pack(side=LEFT, expand=True, fill="x", padx=5)
                self.settings_label_ref_list.append(self.settings_options_labels)

        # call the function to create labels for the optionmenus, this must be before the frame for the optionmenus is created
        create_labels("optionmenus")

        # Create a frame to hold optionmenus
        self.optionmenu_frame = Frame(self.settings_frame, bg=background_color)
        self.optionmenu_frame.pack(fill="x", pady=(5, 0))
        # this is a reference dictonary for the option menus, so we can change them later if needed.
        self.optionmenus_ref_dict = {}

        # this function creates the option menus, it goes through the list and creates a option menu for each item in the list.
        def create_optionmenus():
            optionmenus = [
            # this list contains all the data for the option menus
            # it goes: start text, options, row, collumn
            ["mode", "quiz", "math", 0, 0,],
            ["name", "True", "False", 0, 1],
            ["save", "True", "False", 0, 2],
            ["results", "True", "False", 0, 3],

            ]

            for i in range(len(optionmenus)):
                default_state = StringVar()
                default_state.set(self.config_list[i])  # Set default value to the first option

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
                self.optionmenu.pack(side=LEFT, expand=True, fill="x", padx=5)

                self.optionmenus_ref_dict.update({optionmenus[i][0]: self.optionmenu})

        # create the combobox labels
        create_labels("comboboxes")

        # Create a frame to hold comboboxes
        self.comboboxes_frame = Frame(self.settings_frame, bg=background_color)
        self.comboboxes_frame.pack(fill="x", pady=(5, 0))
        self.comboboxes_ref_dict = {}

        # this function creates the comboboxes, it goes through the list and creates a combobox for each item in the list.
        def create_comboboxes():
            comboboxes = [
            # this list contains all the data for the combomenu
            # it goes: start text, options, row, collumn
            ["amount", "5", "10", "15", "20", 0, 0],
            ["length", "5", "10", "15", "20", 0, 1],
            ["password", "", "", "", "", 0, 2],
            ["color", "grey", "white", "black", "green", 0, 3],
            ]

            # this loop creates the comboboxes, it goes through the list and creates a combobox for each item in the list.
            for i in range(len(comboboxes)):
                counter = i + 4
                default_state = StringVar()
                default_state.set(comboboxes[i][0])  # Set default value to the first option

                self.comboboxes = Combobox(self.comboboxes_frame,
                                           values=[comboboxes[i][1], comboboxes[i][2], comboboxes[i][3], comboboxes[i][4]],
                                           font=("arial", 12),
                                           width=8,
                                           )
                self.comboboxes.pack(side=LEFT, expand=True, fill="x", padx=5)
                self.comboboxes.set(self.config_list[counter])  # Set the default text to the first option

                self.comboboxes_ref_dict.update({comboboxes[i][0]: self.comboboxes})
        # this explains what the two modes do.
        self.settings_mode_info = Label(self.settings_frame,
                                text="The mode setting allows the 'quiz' and " \
                                "'math' modes, quiz will run the" \
                                "questions set in questions.py, while " \
                                "math with randomly generate math " \
                                "questions. Read README.txt for explanation on what" \
                                " the settings do.",
                                font=("arial", "14"),
                                justify="left",
                                wraplength=450,
                                bg=background_color,
                                )
        self.settings_mode_info.pack(pady=(10, 0))
        # frame to hold the buttons
        self.settings_button_frame = Frame(self.settings_frame,
                                    background=background_color)
        self.settings_button_frame.pack(pady=(10, 0))

        # list to hold the buttons, so we can change them later if needed.
        self.button_ref_list = []

        settings_button_details_list = [
        # text, color, command, row, column
        # put your buttons features in this list.
        ["Exit", "#f44336", lambda: restart_quiz(), "0", "0"],
        ["Apply", "#aaaeff", lambda: apply_changes(), "0", "1"],
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
                                command=item[2],
                                anchor="center",
                                justify="center"
                                )
            self.make_button.pack(side=LEFT, expand=True, fill="x", padx=10)
          
        def input_checker(input):
            for i in range(len(input)):
                # Check if the input is empty
                if input[i] == "":
                    self.settings_label_ref_list[i].config(fg="red")
                    self.settings_label.config(fg="red", text="There are settings left blank, the errors are indicated in red.")
                    error = True
                # Check if the input is a number
                if i in [4, 5] and not input[i].isdigit():
                    self.settings_label_ref_list[i].config(fg="red")
                    self.settings_label.config(fg="red", text="There are letters where there shouldnt be, the errors are indicated in red.")
                    error = True
            if error == True:
                return(True)
            else:
                return(False)
            


        # Create the option menus and comboboxes
        create_optionmenus()
        create_comboboxes()
        def apply_changes():
            """
            This function applies the changes made in the settings window.
            It updates the settings.ini file with the new values.
            """
            config = configparser.ConfigParser()
            config.read('settings.ini')
            # Gather all variables starting with self. into a list
            settings_values = [
                self.optionmenus_ref_dict['mode'].cget('text'),
                self.optionmenus_ref_dict['name'].cget('text'),
                self.optionmenus_ref_dict['save'].cget('text'),
                self.optionmenus_ref_dict['results'].cget('text'),
                self.comboboxes_ref_dict['amount'].get(),
                self.comboboxes_ref_dict['length'].get(),
                self.comboboxes_ref_dict['password'].get(),
                self.comboboxes_ref_dict['color'].get()
            ]

            # this is done to reset the label colors to black before checking for errors, so that if there
            # was a previous error that was fixed, the label color will be reset to black.
            for i in range(len(settings_values)):
                 self.settings_label_ref_list[i].config(fg="black")

            if input_checker(settings_values):
                 return
            
            # Assign the values from the list to the config
            config['settings']['mode'] = settings_values[0]
            config['settings']['name'] = settings_values[1]
            config['settings']['save'] = settings_values[2]
            config['settings']['results'] = settings_values[3]
            config['settings']['amount'] = settings_values[4]
            config['settings']['difficulty'] = settings_values[5]
            config['settings']['password'] = settings_values[6]
            config['settings']['color'] = settings_values[7]




            # Write the updated settings back to the file
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)

            # Close the settings window and restart the quiz
            self.settings_window.destroy()
            restart_quiz()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    
    Quiz(root)
    root.mainloop(
    )