import random
import time

response=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q","R","S","T","U"]

def teil1():
    question=raw_input("Whats on your mind: ")
    print "let me think about your question"
    time.sleep(4)
    print random.choice(response)
    teil2()

def teil2():
    print "do you want to ask me again about anything?"
    userchoice=raw_input("yes or no: ")
    if userchoice =="yes":
        teil1()
    elif userchoice=="no":
        print "ok, have a nice day"
    else:
        print "error with the input. answer again"
        teil2()
teil1()