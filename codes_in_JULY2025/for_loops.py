#for loops with else statement and break statement
for x in range(1,51):
    if x == 37:
        print("Found 37, breaking the loop.")
        break #stop the loop when x is 37
    print(x)
else:
    print("Loop completed without finding 37.")

#testng

for i in range(5):
    print("Printing")
    if i == 2:
        continue #skips when i=2
    print(i)