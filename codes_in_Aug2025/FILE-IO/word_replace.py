with open("donkey.txt") as f:
    x = f.read()

y = x.replace("Donkey", "###")

with open("donkey.txt", "w") as f:
    f.write(y)

