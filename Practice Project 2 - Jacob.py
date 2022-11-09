

answer = "Applesauce"
guessedanswer = input("Guess letter: ")
stringp1 = "You have"
stringp2 = "guesses left"

print("_ " * 10 '''
''')

def guess():
    health = int(6)
    wrongguess = int(1)
    if guessedanswer in answer:
        print(" {} is in {}".format(guessedanswer, answer)) 
    else:
        print("Guess is wrong")
        life = health - wrongguess
        print(stringp1, life, stringp2)


guess()
