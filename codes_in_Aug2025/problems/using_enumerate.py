l = ["Hello", 2, 3, "Four", 5, 6, 7]

for index, value in enumerate(l):
    if index==2 or index==4 or index==6:
        print(f"The element at position {index+1} is: {value}")