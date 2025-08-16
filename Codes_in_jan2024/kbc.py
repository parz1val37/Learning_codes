qns = ["q1: 3 + 5 =","q2: 4 * 5 =","q3: 9 / 3 ="]
score = 0
print(qns[0])
a = int(input("ENTER ANSWER:"))
match a:
    case _ if a == 8:
        print("RIGHT")
        score += 1
    case _:
        print("WRONG")

print(qns[1])
b = int(input("ENTER ANSWER:"))
match b:
    case _ if b == 20:
        print("RIGHT")
        score += 1
    case _:
        print("WRONG")
        
print(qns[2])
c = int(input("ENTER ANSWER:"))
match c:
    case _ if c == 3:
        print("RIGHT")
        score += 1
    case _:
        print("WRONG")

print(f"your total score is: {score}/3")