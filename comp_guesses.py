# So here basically, user has a secret number and the computer has to guess it. So the computer has a range of numbers 
# to work with. Hence defining a high and low initially. And have a comment ie to tell the comp if its too high or 
# too low. So defining a comment variable for it. 
import random

def comp_guess(x):
    guess = 0
    low = 1
    high = x
    comment = ""
    while comment != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high. Cause low = high

        comment = input(f"Is {guess} too High (H), too Low (L), or correct (C)???").lower()
        if comment == "h":
            high = guess - 1
        if comment == "l":
            low = guess + 1
    
    print(f"Yayyaa!! BINGO!! The computer guess the, {guess}, correctly")
    
comp_guess(1000)