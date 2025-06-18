
# random math questions generator
import random
import quiz_gui_v2 as t
import configparser






# This is where the questions and answers are, put them in the quotes.
Questions = [
    "What is the capital city of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the chemical symbol for gold?",
    "Which planet is known as the Red Planet?",
    "In what year did the Titanic sink?",
    "Who painted the Mona Lisa?",
    "What is the largest organ in the human body?",
    "Which country is famous for the maple leaf?",
    "What is the square root of 144?",
    "Who is known as the father of modern physics?"
]

# This is where the answers are, put them in the quotes, add extra answers by separating them with a comma.
# empty answers will be ignored, so don't put them in the quotes. use a word like "nothing" or "none" 
# if you want to have an empty answer.
Answers = [
    ["paris", "paris, france", "the city of paris"],
    ["william shakespeare", "shakespeare", "w. shakespeare"],
    ["au", "gold"],
    ["mars", "the red planet"],
    ["1912", "the year 1912"],
    ["leonardo da vinci", "da vinci", "leonardo", "leonardo da-vinci"],
    ["skin", "the skin", "human skin"],
    ["canada", "the maple leaf country"],
    ["12", "twelve"],
    ["albert einstein", "einstein", "professor einstein", "dr einstein"]
]







"""

Questions = [
    "How many apples are in a dozen apples?",
    "What's the color of the sky on a clear day?",
    "How many legs does a dog have?",
    "What's 2 + 2?",
    "What do you call the frozen form of water?",
    "What's the opposite of 'hot'?",
    "What animal goes 'meow'?",
    "What fruit's typically red and often associated with doctors?",
    "How many days are in a week?",
    "What's the first letter of the alphabet?"
]


# This is where the answers are, put them in the quotes, add extra answers by separating them with a comma.

Answers = [
    ["12", "twelve", "1", "one", "dozen", "a dozen", "a"],
    ["blue", "a"],
    ["4", "four", "a"],
    ["4", "four", "a"],
    ["ice", "the frozen form of water", "a"],
    ["cold", "toh", "a"],
    ["cat", "cats", "human", "humans", "a"],
    ["apple", "apples", "a"],
    ["7", "seven", "a"],
    ["a", "t"],
]
"""
try:
    config = configparser.ConfigParser()
    config.read('settings.ini')
    difficulty = int(config['settings']['difficulty'])
    amount = int(config['settings']['amount'])
except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
    difficulty = 2
    amount = 10

# dificulty is the number of numbers in the question, so a difficulty of 4 would be 4 numbers and 3 signs
# amount is the number of questions to generate, so if amount is 10, it will generate 10 questions

# the lists to store the questions and answers
Math_Answers = []
Math_Questions = []
# the list of operators to choose from
# this can be expanded to include more operators if desired
operator = ['+', '-', '*', '/']
def gen_questions():
    for i in range(amount):
        # variables are set to default values for each question, 
        counter = 0
        question = []
        answer = ""
        finished_question = ""
        while counter < difficulty:
            # randomly select a sign and a number
            sign = operator[random.randint(0, 3)]
            num1 = random.randint(1, 20)

            # if its the last number in the question, don't add a sign
            if counter == difficulty - 1: 
                component = f"{num1}"
            # otherwise, add a sign
            else:
                component = f"{num1} {sign} "
            # add the component to the question
            question.append(component)
            if counter == difficulty - 1:
                # combine the question list into a string
                finished_question = ''.join(question)

                # evaluate the question to get the answer
                answer = eval(str(finished_question))
                # check if the answer is divisable into a integer (no stupid decimals)
                # will append the question and answer to the lists if it is
                if answer.is_integer():
                    Math_Answers.append([str(int(answer))])
                    Math_Questions.append(finished_question)
                # if not, reset the question and answer variables
                else:
                    question = []
                    answer = ""
                    finished_question = ""
                    # could not find a better way to reset the counter to 0 besides setting it to -1 so it is incremented to 0 at the end of the loop
                    counter = -1

            counter += 1