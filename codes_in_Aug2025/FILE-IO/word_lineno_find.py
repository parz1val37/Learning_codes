#--------Give the 'line no' for first occurance of given word.
word = input("Ente the word to get it\'s line no: ")

with open("Qfile.txt") as f:
    lines = f.readlines()

line_no = 1

for line in lines:
    if word.lower() in line.lower():
        print(f"The word \'{word}\' is present in line no: {line_no}")
        break
    line_no += 1

else:
    print(f"The word \'{word}\' is not in the \'Qfile.txt\'")

