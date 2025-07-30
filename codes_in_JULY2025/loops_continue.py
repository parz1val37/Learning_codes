l = [1, 3,"Game",True,'Hola']
for i in l:
    if i == "Game":
        print("Found Game, continuing to next iteration.")
        continue  # Skip the rest of the loop for this iteration
    print(i)

