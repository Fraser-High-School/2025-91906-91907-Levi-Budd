Hello, this is my program called "Levi's Quiz Helper", you can use it to either quiz yourself, set up questions for others to do,
or to have it randomly generate math questions of a custom difficulty. In questions.py you can set up both the questions and the answers, just plop
your questions in the quotes, and put the answers down below. You can also access the settings window by pressing "Start Quiz" after writing the password
into the entry box, this password by default is "1234", but in the settings window you can change it to anything you want.

here are explanations for what the settings do

mode:
Sets the quiz mode. Use 'quiz' to run questions and answers from questions.py, or 'math' to generate random math problems based on the difficulty and amount settings.

amount:
Sets how many questions or math problems will be generated. Only whole numbers (integers) are allowed.

difficulty:
Determines how complex the math problems are. For example, a difficulty of 2 generates problems like 16 + 7 or 20 / 5. A difficulty of 3 generates longer problems like 12 + 34 * 2 or 9 - 5 + 1. Only whole numbers are allowed.

password:
The password required to access the settings menu. Enter this before pressing "start quiz". Any string can be used.

name:
If set to True, the program will prompt for the quiz taker's name. If set to False, it will not ask for a name.

save:
If set to True, the results will be saved to results.txt. If set to False, results will not be saved.

results:
If set to True, the program will show results inside the application. If set to False, results will not be shown in the program.

color:
Sets the background color. You can use any color accepted by Tkinter, including standard color names (like grey) or hex codes (like #000000 for black).