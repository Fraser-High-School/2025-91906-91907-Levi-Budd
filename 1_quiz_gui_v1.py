# importing tkinter, time, 
# and questions & answers from questions.py
from tkinter import *
from time import *
import questions as q
class Quiz():
    
    """
    tool is used to quiz people using the questions and answers set by the operator,
    it takes the questions and answers from 'questions.py'
    """
    def __init__(self):
        # backround_color variable is the color grey used for the backround
        # makes it so you can change every widgets backround color
        # at the same time.
        global background_color
        background_color = "#b3b3b3"
        
        
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
        self.quiz_instructions = Label(self.quiz_frame,
                                  text="Press start quiz to start answering questions!",
                                  font=("arial", "20"),
                                  wraplength=250, width=20,
                                  bg=background_color,
                                  )
        self.quiz_instructions.grid(row=4)

        # makes the frame all the buttons are stored in
        self.button_frame = Frame(self.quiz_frame,
                                bg=background_color,)
        self.button_frame.grid()

        # These two functions start the buttons up, case is set as default to make
        # the base buttons.
        self.buttonswitch_left("default")
        self.buttonswitch_right("default")
        


    def buttonswitch_right(self, case):
        button_details_list = [
            # text, color, command, row, column
            # put your buttons features in list.
            ["results", "#aaaeff", lambda:print("not implemented yet"), "1"],
            ["finish", "#ffe600", lambda:self.buttonswitch_right("default"), "1"],
        ]
        self.button_ref_list = []

        if case == "default":
        #creates the default button that appears on program startup
                self.make_button = Button(self.button_frame,
                                        text=button_details_list[0][0],
                                        bg=button_details_list[0][1],
                                        fg="#000000",
                                        font=("Arial", "20", "bold"),
                                        width=9,
                                        command=button_details_list[0][2]
                                        )
                self.make_button.grid(padx=3, row=0, column=1)
                

        elif case == "begin":
        # makes the finish button, it runs when the start buttons gets pressed
                self.make_button = Button(self.button_frame,
                                        text=button_details_list[1][0],
                                        bg=button_details_list[1][1],
                                        fg="#000000",
                                        font=("Arial", "20", "bold"),
                                        width=9,
                                        command=button_details_list[1][2]
                                        )
                self.make_button.grid(padx=3, row=0, column=1)
                


    def buttonswitch_left(self, case):
        button_details_list = [
            # text, color, command, row, column
            # put your buttons features in list.
            ["Start Quiz", "#00ff08", lambda:self.buttonswitch_left("begin"), "0"],
            ["Submit", "#00ff08", lambda:self.buttonswitch_left("end"), "0"],
            ["Submit", "#00ff08", lambda:print("sample text"), "0"],
        ]
        self.button_ref_list = []

        if case == "default":
        #creates the default start quiz button that appears on program startup
                self.make_button = Button(self.button_frame,
                                        text=button_details_list[0][0],
                                        bg=button_details_list[0][1],
                                        fg="#000000",
                                        font=("Arial", "20", "bold"),
                                        width=9,
                                        command=button_details_list[0][2]
                                        )
                self.make_button.grid(padx=3, row=0, column=0)
                

        elif case == "begin":
        # makes the submit button when the start quiz button is pressed, it also creates the finish button
                self.make_button = Button(self.button_frame,
                                        text=button_details_list[1][0],
                                        bg=button_details_list[1][1],
                                        fg="#000000",
                                        font=("Arial", "20", "bold"),
                                        width=9,
                                        command=button_details_list[1][2]
                                        )
                self.make_button.grid(padx=3, row=0, column=0)

                self.buttonswitch_right("begin")
                

        elif case == "end":
        # disables the submit button when the submit button is pressed, signals end of quiz
        # ill make it so that only triggers at the last question
            self.make_button = Button(self.button_frame,
                                    text=button_details_list[2][0],
                                    bg=button_details_list[2][1],
                                    fg="#000000",
                                    font=("Arial", "20", "bold"),
                                    width=9,
                                    state="disabled",
                                    command=button_details_list[2][2]
                                    )
            self.make_button.grid(padx=3, row=0, column=0)
            
                

        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    
    Quiz()
    root.mainloop(
    )