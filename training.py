# Global Variables
score = 0
current_question = 0

filename = "highscore.txt"

#### Start of functions ###
def Question1():
    global score
    global current_question

    current_question += 1
    default_answer = "tnsmsbbn"

    answer1 = input("Please enter the initials on how you memorize data structures:").lower() 

    if answer1 == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")

    Question2()

def Question2():
    global score
    global current_question

    current_question += 1

    default_answer = "13312131"

    answer = input("How many types of answers does each type have:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")
    Question3()

def Question3():
    global score
    global current_question

    current_question += 1
    default_answer = "string"

    answer = input("What data is text in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")

    Question4()

def Question4():
    global score
    global current_question

    current_question += 1
    default_answer = "int, float, complex"

    answer = input("What are numeric types in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")
    
    Question5()

def Question5():
    global score
    global current_question

    current_question += 1
    default_answer = "list, tuple, range"

    answer = input("What are sequence types in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")

    Question6()

def Question6():
    global score
    global current_question

    current_question += 1
    default_answer = "dict"

    answer = input("What are mapping types in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")
    Question7()

def Question7():
    global score
    global current_question

    current_question += 1
    default_answer = "set, frozenset"

    answer = input("What are set types in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")

    Question8()

def Question8():
    global score
    global current_question

    current_question += 1
    default_answer = "bool"

    answer = input("What are boolean types in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")

    Question9()

def Question9():
    global score
    global current_question

    current_question += 1
    default_answer = "bytes, bytearray, memoryview"

    answer = input("What are binary types in python:\n")

    if answer == default_answer:
        score += 1
        print(f"\nCorrect answer your score is: {current_question}\{score}\n")
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")
    
    Question10()

def Question10():
    global score
    global current_question

    current_question += 1
    default_answer = "NoneType"

    answer = input("What are none types in python:\n")

    if answer == default_answer:
        score += 1
    
    else:
        print(f"\nSorry the correct answer would have been: {default_answer}\n")

    print(f"\nYour total score is: {current_question}\{score}\n")
    write_to_file(current_question,score)

def write_to_file(current_question, score):
    global filename
    f = open(filename, "a")
    f.write(f"{current_question}/{score}\n")

# Programatic flow
while True:
    menu = input('''Please enter what you want to learn:
                 1. Data Structures\n''')
    
    if menu == '1':
        Question1()