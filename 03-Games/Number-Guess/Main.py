import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number I am thinking of it is between 1 and {x} '))
        if guess < random_number:
            print("Sorry, that is too low! Guess again")
        elif guess > random_number:
            print("Sorry, guess again, too high!")
    print (f"Well done, you've guessed correctly! The number was {random_number}!!!")        

guess(100)