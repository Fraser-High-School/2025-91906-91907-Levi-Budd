from tkinter import *
import questions as q
class Quiz():
    """
    This tool is used to quiz people on stuff, it take the questions and
    answers from 'questions.py'
    """
    def __init__(self):
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        self.quiz_heading = Label(self.quiz_frame,
                                  text="Quiz Program",
                                  font=("arial", "24"))
        self.quiz_heading.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    Quiz()
    root.mainloop(
    )