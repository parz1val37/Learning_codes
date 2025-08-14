def math_quiz():
    print("Welcome to the Math Quiz!")
    print("You will be asked a simple math question.")
    print("What is 2 + 2")
    x = int(input("Please enter your answer: "))
    # Using match-case to handle different operations
    match x:
        case 4:
            print("Correct! 2 + 2 equals 4.")
        case _:
            print("Incorrect.")

math_quiz()