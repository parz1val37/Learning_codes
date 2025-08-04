#------takes the input and save it in the file
#type any poem or sentence.
# y = input("Enter the text u wanna add: ")     #----comment out and use the code--------#
# with open("poem.txt", "w") as p:
#     p.write(y)

#finds if the given word is in the file or not
with open("poem.txt") as r:
    k = r.read()
    x = input("Type the word u wanna search: ")
    if x in k:
        print(f"{x} is in the poem text file.")
    else:
        print(f"{x} is not in the poem text file.")

# EVERYTIME this code rund its update text file with given texts.