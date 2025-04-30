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
        question = "Press start quiz to start answering questions!"
        self.quiz_instructions = Label(self.quiz_frame,
                                  text=question,
                                  font=("arial", "22"),
                                  wraplength=350, width=20,
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
            ["results", "#aaaeff", lambda:print("take to results page"), "normal"],
            ["finish", "#ffe600", lambda:print("tell results"), "normal"],
        ]
        self.right_button_ref_list = []

        if case == "default":
                state = 0
        elif case == "finish":
                state = 1

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
                


    def buttonswitch_left(self, case):
        button_details_list = [
            # text, color, command, row, column
            # put your buttons features in list.
            ["Start Quiz", "#00ff08", lambda:self.buttonswitch_left("begin"), "normal"],
            ["Submit", "#00ff08", lambda:self.question_answer(), "normal"],
            ["Submit", "#00ff08", lambda:print("sample text"), "disabled"],
        ]
        self.left_button_ref_list = []
        counter = 0
        if case == "default":
                state = 0
        elif case == "begin":
                self.buttonswitch_right("finish")
                state = 1
        elif case == "end":
                self.buttonswitch_right("default")
                state = 2

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
                

    counter = 0
    length = len(q.Questions)
    def question_answer(self):
            if self.counter < self.length:
                question = q.Questions[self.counter]
                self.counter += 1
                self.quiz_instructions.config(text=question, fg="#9C0000")
                
                print(self.left_button_ref_list[0])
                
                print(question)
                
            elif self.counter >= self.length:
                self.buttonswitch_left("end")



                #self.left_button_ref_list[0].config(command=self.question_answer())
                


            
            
          
                
    
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    
    Quiz()
    root.mainloop(
    )