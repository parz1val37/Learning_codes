#not so as game but it helps to know more about file attributes.
import random

def game():
    print("You are in the game...")
    score = random.randint(1,69)
    print(f"Your score is {score}")

    with open("Hi-score.txt") as f:
        hscore = f.read()
        if hscore!="":
            hscore = int(hscore)
        else:
            hscore = 0
    
    if (score>hscore):
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))

    return score

game()