import random

def guess(x):
    random_no = random.randint(1, x)
    guess = 0
    while guess != random_no:
        guess = int(input(f"Guess A Number from 1 and {x}: "))
        if guess < random_no:
            print("Sorry, The Guess is too Low. Try Again!")
        elif guess > random_no:
            print("Sorry, The Guess is too High. Try Again!")
    print(f"BINGO!!! The number is {random_no}")

guess(7)




            