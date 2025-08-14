l = [3, 37, 69, 71, 21]

#---Normally---
# for i in range(len(l)):
#     print(f"Item at index {i} is {l[i]}")
#-------OR----
# index = 0
# for i in l:
#     print(f"Item at index {index} is {i}")
#     index += 1

#----Using enumerate:

for index, i in enumerate(l):
    print(f"Item at index {index} is {i}")