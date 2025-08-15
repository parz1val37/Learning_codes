try:
    with open("1.txt") as f1:
        content1 = f1.read()
    print("Content of 1.txt:", content1)
except:
    print("Error opening 1.txt")

try:
    with open("2.txt") as f2:
        content2 = f2.read()
except:
    print("Error opening 2.txt")

try:
    with open("3.txt") as f3:
        content3 = f3.read()
except:
    print("Error opening 3.txt")

# print("Content of 2.txt:", content2)