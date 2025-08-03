#remove a desire word from a predefined list.

l = ["Sanaullah", "Spider", "Games", "Books", "Coding", "Python"]
print(f"list is:\n{l}")

def remove_word():
    k = input("Enter the word you want to remove from the list: ")
    if k in l:
        l.remove(k)
        print(f"New list now is:\n{l}")
    else:
        print(f"{k} is not in the list.")
    return

remove_word()

#removing a word from a list made by user

k = input("Enter the words of a list seperated by commas: ")
L = k.split(',')
print(f"list is:\n{L}")

def remove_wrd():
    X = input("Enter the word you want to remove from the list: ")
    if X in L:
        L.remove(X)
        print(f"New list now is:\n{L}")
    else:
        print(f"{X} is not in the list.")
    return

remove_wrd()