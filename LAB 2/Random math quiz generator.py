#Write a program that gives simple math quizzes. The program should display two random
#numbers that are to be added, such as:
#247
#+ 129
#The program should allow the student to enter the answer. If the answer is correct, a message of
#congratulations should be displayed. If the answer is incorrect, a message showing the correct
#answer should be displayed.

import random

random_int = random.randint(100, 900)
random_int2 = random.randint(100, 900)

print(random_int,"\n+",random_int2)

def function(user):
    if user == random_int2+random_int:
        print("congratulations!")
    else: 
        print("Not correct.The correct answer is:",(random_int2+random_int))

user=int(input("Input your answer"))

function(user)
