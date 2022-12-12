start = True


def game():
    if start == True:
        import random
        from collections import Counter

        someWords = '''abarth acura alpine aprillia audi bmw bently bugatti buick cadillac cheverolet chrysler dodge ducati ferrari fiat ford geely honda hyosung 
        hyundai infinity jaguar jeep ktm kawaski kia koenigsegg lamborghini lexus lincoln lotus maserati mazda mclaren mercedes mitsubishi mitsuoka nio nissan 
        norton pagani porsche ram renault rezvani scion seat skoda smart subaru tata tesla toyota triumph ural vauxhall volkswagon yamaha'''
        someWords = someWords.split(' ')
        word = random.choice(someWords)

    if __name__ == '__main__':
        print()
        print('Guess the word! HINT: The word is a name of a car manufacturer')
     
        for i in word:
            print('_', end = ' ')       
        print()

        playing = True
        guessedletter = ''               
        chances = len(word) + 2
        correct = 0
        flag = 0
        try:
            while (chances != 0) and flag == 0: 
                print()
                chances -= 1
 
                try:
                    guess = str(input('Enter a letter to guess: '))
                except:
                    print('Enter only a letter!')
                    continue

                if not guess.isalpha():
                    print('Enter only a LETTER')
                    continue
                elif len(guess) > 1:
                    print('Enter only a SINGLE letter')
                    continue
                elif guess in guessedletter:
                    print('You have already guessed that letter')
                    continue

                if guess in word:
                    k = word.count(guess) 
                    for _ in range(k):   
                        guessedletter += guess 

                for char in word:
                    if char in guessedletter and (Counter(guessedletter) != Counter(word)):
                        print(char, end = ' ')
                        correct += 1
                    elif (Counter(guessedletter) == Counter(word)):
                        print("The word is: ", end=' ')
                        print(word)
                        flag = 1
                        print('You win!')
                        print()
                        endgame = input("Would you like to continue(Y / N)?")
                        if endgame == "Y" or 'y':
                            return game()
                        else:
                            print("See ya!")
                            quit()
                    else:
                        print('_', end = ' ')
 
            if chances <= 0 and (Counter(guessedletter) != Counter(word)):
                print()
                print('L! Try again..')
                print('The word was {}'.format(word))
                print()
                endgame = input("Would you like to continue(Y / N)?")
                if endgame == str('Y' or 'y') :
                    print('lets play')
                    return game()
                else:
                    print('Bye Bye')
                    quit()
                # if endgame == "Y" or "y":
                #     print("Lets play!")
                #     quit()
                # else:
                #     print("See ya!")
                #     quit()
            
        except KeyboardInterrupt:
            print()
            print('See ya! Try again.')

game()



#Monkeism
