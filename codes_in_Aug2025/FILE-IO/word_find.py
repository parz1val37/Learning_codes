#------Search for the word irrespective of how its written-----#

word = input("Enter the word you want to search for in \'Qfile.txt\': ")

with open("Qfile.txt") as f:
    content = f.read()

if word.lower() in content.lower():
    print(f"The word \'{word}\' is in the \'Qfile.txt\'")
else:
    print(f"The word \'{word}\' is not in the \'Qfile.txt\'")

