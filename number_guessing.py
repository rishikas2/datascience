import random

n= random.randint(1,100)
while True:
    guess= int(input("Guess a number between 1 and 100: "))
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
    