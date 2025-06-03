
# random math questions generator
import random
difficulty = 4
amount = 10

signs = []
Math_Answers = []
Math_Questions = []
operator = ['+', '-', '*', '/']
def gen_questions():
    for x in range(amount):
        question = []
        counter = 0
        while counter < difficulty:
            sign = operator[random.randint(0, 3)]
            num1 = random.randint(1, 20)
            if counter == difficulty - 1: 
                component = f"{num1}"

            else:
                component = f"{num1} {sign} "

            question.append(component)
            
            if counter == difficulty - 1:
                finished_question = ''.join(question)
                answer = eval(str(finished_question))
                if answer.is_integer():
                    Math_Answers.append(answer)
                    Math_Questions.append(finished_question)
                    counter += 1
                else:
                    question = []
                    answer = ""
                    
            

gen_questions()

for x in range(len(Math_Questions)):
    print(x)
    print(f"What is {Math_Questions[x]}")
    print(f"Answer is {Math_Answers[x]}")
print(len(Math_Questions))
print(Math_Questions)




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