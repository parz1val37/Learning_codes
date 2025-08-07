with open("ofile.txt") as f:
    content = f.read()

with open("0file.txt") as f:
    context = f.read()

if context == content:
    print("Both contains the same thing.")
else:
    print("Both files are different.")