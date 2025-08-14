l = [1, 3, 5, 7, 9]

#---------using for loop----
# squared_l = []
# for i in l:
#     squared_l.append(i ** 2)
# print(squared_l)

#---------using list comprehension----
squared_l_comp = [i ** 2 for i in l]
print(squared_l_comp)

add_3_in_l = [i + 3 for i in l]
print(add_3_in_l)