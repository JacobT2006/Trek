
answer = "Earthbound"
statement = """The answer is: (1 2 3 4 5 6 7 8 9 10)"""

print(statement)

guessedanswer = input("Guess letter: ")

def guess():
    health = int(6)
    wrongguess = int(1)

    guessedanswer = input("Guess letter: ")

    if guessedanswer in answer:
        print(" {} is correct. ".format(guessedanswer)) 

        if guessedanswer == "e":
            print(1)
            answer[-20:] = "E"
            print(statement)
        elif guessedanswer == "a":
            statement.replace('2', 'a')
            print(statement)
        elif guessedanswer == "r":
            statement.replace('3', 'r')
            print(statement)
        elif guessedanswer == "t":
            statement.replace('4', 't')
            print(statement)
        elif guessedanswer == "h":
            statement.replace('5', 'h')
            print(statement)
        elif guessedanswer == "b":
            statement.replace('6', 'b')
            print(statement)
        elif guessedanswer == "o":
            statement.replace('7', 'o')
            print(statement)
        elif guessedanswer == "u":
            statement.replace('8', 'u')
            print(statement)
        elif guessedanswer == "n":
            statement.replace('9', 'n')
            print(statement)
        elif guessedanswer == "d":
            statement.replace('10', 'd')
            print(statement)
    elif guessedanswer not in answer:
        print("Guess is wrong")
        life = health - wrongguess
        print("You have", life, "guesses left")
        return guess()
    else:
        return guess()

    

    if health <= 0:
        print('GAME OVER')


guess()

#Monkeism
