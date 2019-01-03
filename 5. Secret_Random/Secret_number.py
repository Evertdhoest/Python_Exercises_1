def main():
    ##Secret Calculator with hardcoded number

    #import random library
    from random import randint

    #make secret number random
    secret = randint(1,100)

    ##For testing purposes use : print(secret)

    #Ask for a guess
    guess = input("Guess the secret number: ")

    #loop guessing
    while True:

        #check if guess is digit between 1-100
        while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
            print("This input is incorrect")
            guess = input("Please choose a number between 1 and 100: ")
            continue

        #check results
        if int(secret) == int(guess):
            print("Correct, the number was " + str(secret))
            break
        elif int(secret) < int(guess):
            print("Wrong, the number was lower")
            guess = input("Please choose again: ")
        elif int(secret) > int(guess):
            print("Wrong, the number was higher")
            guess = input("Please choose again: ")
if __name__ == "__main__":
    main()