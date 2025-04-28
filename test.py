from tkinter import *
from time import *
import questions as q
class Quiz():
    
    """
    This tool is used to quiz people on stuff, it take the questions and
    answers from 'questions.py'
    """
    def __init__(self):
        # this variable is the color grey used for the backround
        # makes it so you can change every widgets backround color
        # at the same time.
        background_color = "#b3b3b3"
        
        # this just sets the size of the window
        root.geometry("360x300")
        root.wm_attributes("-transparentcolor", 'grey') 
        root.configure(bg=background_color)

        # the frame holding the entire gui is created here
        self.quiz_frame = Frame(padx=10, pady=10, bg=background_color)
        self.quiz_frame.grid()

        # the heading is made here
        self.quiz_heading = Label(self.quiz_frame,
                                  text="Quiz Program",
                                  font=("arial", "32"),
                                  bg=background_color,
                                  )
        self.quiz_heading.grid(row=0)
        
        # the entrybox where you put in your answer is here
        self.quiz_entry = Entry(self.quiz_frame,
                                  font=("Arial", "38"),
                                  width=(12),
                                  )
        self.quiz_entry.grid(row=2, padx=1, pady=1)
        
        self.quiz_entry_instructions_shadow = Label(self.quiz_frame,
                                  text="Please enter your answer above",
                                  font=("arial", "14"),
                                  bg="transparent",
                                  )
        self.quiz_entry_instructions_shadow.place(x=30, y=120)

        self.quiz_entry_instructions_color = Label(self.quiz_frame,
                                  text="Please enter your answer above",
                                  font=("arial", "14"),
                                  fg="#FFFF00",
                                  bg=background_color,
                                  )
        self.quiz_entry_instructions_color.place(x=5, y=0, in_=self.quiz_entry_instructions_shadow)
        # this is the end of the entry instructions frame

        #
        self.quiz_instructions = Label(self.quiz_frame,
                                  text="blah",
                                  font=("arial", "32"),
                                  bg=background_color,
                                  )
        self.quiz_instructions.grid(row=4, pady=30)

        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    
    Quiz()
    root.mainloop(
    )