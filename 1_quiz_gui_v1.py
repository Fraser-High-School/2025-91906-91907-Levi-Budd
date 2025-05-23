# importing tkinter, time, 
# and questions & answers from questions.py
from tkinter import *
from time import time, strftime, localtime
import time
import questions as q
# os is imported to open the results file
import os

class Quiz():
    
    """
    this tool is used to quiz people using the questions and answers set by the operator,
    it takes the questions and answers from 'questions.py'
    """
    
    
    def __init__(self, root):
        # backround_color variable is the color grey used for the backround
        # makes it so you can change every widgets backround color
        # at the same time.
        global background_color
        background_color = "#b3b3b3"
        # results will hold all the data, this includes time taken, date, questions answered, and correct answers.
        self.results = []
        # these track time and date.
        self.start_time = 0.0
        self.start_date = ""
        # these variables are used to keep track of the variables to write to results.txt.
        # they have to be set outside of the function so they arent reset every time the function is called.
        self.counter = 0
        self.length = len(q.Questions)
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
        root.wm_attributes("-transparentcolor", 'grey') 
        root.configure(bg=background_color)
       

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
        Results_window = ResultsWindow(root)
                


    

    def question_answer(self):
            
            #this checks if the counter (amount of questions answered) is less than the length of the question list.
            # if it is, it will show the next question and continue the quiz,
            # otherwise it will disable the submit button and end the quiz.
            data_list = []
            


            if self.counter == 0:
                self.quiz_instructions.config(text="Please submit your name.")
                root.bind('<Return>', lambda event: self.question_answer())
                if self.name_said == True:
                    # this is where the name is set, it is set to the entry box.
                    self.name = self.quiz_entry.get()
                    self.name = self.name[0:self.answer_length]
                    self.quiz_entry.delete(0, END)
                    self.quiz_entry_instructions_color.config(text="Please enter your answer above", fg="#FFFF00")
                    self.quiz_instructions.config(text="Press start quiz to start answering questions!")
                    self.name_done = True
                self.name_said = True


            if self.name_done == True:
                if self.counter < self.length:
                    # Bind Enter key to submit the answer.
                    # i do this here so that it only binds when the quiz is actually started.
                    if self.counter == 0:
                        self.start_taken_time = time.time()

                    question = q.Questions[self.counter]
                    self.quiz_instructions.config(text=question, fg="#9C0000")

                # this statement check wether the answer is correct or not, assuming that the counter is above 1
                # so that it doesnt run when the quiz is first started.
                if self.counter > 0:
                    # counter_less_1 is used because lists start at 0, not 1.
                    counter_less_1 = self.counter - 1
                    # block below sets answer to lowercase, remove leading and trailing spaces, and limit to first 30 characters.
                    answer = self.quiz_entry.get().strip().lower()
                    answer = answer[0:self.answer_length]
                    self.quiz_entry_instructions_color.config(text="Please enter your answer above", fg="#FFFF00")

                    # appends the question number, question text, and answer to the data_list.
                    data_list.append([self.counter, q.Questions[counter_less_1], answer])

                    # this clears the entry box so you can enter the next answer, gets the correct answer.
                    self.quiz_entry.delete(0, END)
                    correct_answer = q.Answers[counter_less_1]

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
                    print(data_list)

                # increment counter by 1 to move to the next question
                self.counter += 1

                # ends quiz if counter is greater than length of question list.
                if self.counter > self.length:
                    self.buttonswitch_left("end")
                    # may remove self.openresults() here. idk
                    self.open_results()
                    self.quiz_entry.config(state=DISABLED)
                    self.quiz_entry_instructions_color.config(text="Quiz Finished! go to results page for results!", fg="#00FFFF")


                  
                    




    def write_to_file(self, data):
        with open("results.txt", "a") as r:
            # Loop through the data to write each question's details
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            elapsed_minutes = int(elapsed_time // 60)
            elapsed_seconds = round(elapsed_time % 60, 2)
            date = self.start_date
            

            
            
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
            # this block writes the summary results to summart_results.txt.
            
            with open("summary_results.txt", "a") as r:
 
                sum_date = strftime("%m-%d", localtime())
                r.write(f"""{sum_date}: {self.correct}/{self.length} Questions Correct.\n""")
                
            

class ResultsWindow():
    """
    This class creates the results window, which shows the results of the quiz.
    """

    def __init__(self, parent):
        
        self.results_window = Toplevel(parent)
        self.results_window.title("Results")
        self.results_window.geometry("360x425")
        self.results_window.configure(bg=background_color)

        self.results_frame = Frame(bg=background_color, master=self.results_window)
        self.results_frame.grid(sticky="n")
        self.results_window.grid_rowconfigure(0, weight=1)
        self.results_window.grid_columnconfigure(0, weight=1)
        
        self.results_heading = Label(self.results_frame,
                                text="Results",
                                font=("arial", "25"),
                                
                                bg=background_color,
                                )            
        self.results_heading.grid(row=0, column=0, sticky="n")

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

        self.results_info = Label(self.results_frame,
                                text="You can see more in-depth results (what questions were wrong specifically) by going to the file. If the box is yellow, then there are more results in the file than shown here.",                                       
                                font=("arial", "14"),
                                justify="left",
                                wraplength=350,
                                bg=background_color,
                                )
        self.results_info.grid(row=3, column=0)

        self.results_button_frame = Frame(self.results_frame,
                                    background=background_color)
        self.results_button_frame.grid(sticky="ew", row=4)
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





                


            
            
          
                
    
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    
    Quiz(root)
    root.mainloop(
    )