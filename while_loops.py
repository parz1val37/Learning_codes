#iterate contents of loop using while loop taking inputs from user
# l =  ["Parz1", "Game","KEY","Stone","Random"]
l = []
x1 = input("Enter a list of items separated by commas: ")
l = x1.split(',')

x = 0
while x < len(l):
    print(f"Entered at index: {x} item in list is: {l[x]}")
    x += 1

