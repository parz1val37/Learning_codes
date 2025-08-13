from random import randint

k = randint(1, 100)

def guess_number():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")
    
    guess = 1
    x = -1
    while x != k:
        x = int(input(f"Enter your {guess} guess: "))
        if x < k:
            print("Too low! Try again.")
            guess += 1
        elif x > k:
            print("Too high! Try again.")
            guess += 1
        else:
            print(f"Congratulations! You've guessed the number {k} correctly in {guess} attempts.")

guess_number()