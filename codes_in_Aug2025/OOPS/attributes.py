class test:
    x = 3

y = test()
print(y.x)  # instance attribute is not present

y.x = 4     # instance attribute is created
print(y.x)  # now it prints the instance attribute

#-----instance attribute is printed but class attribute is not changed.
print(test.x)  # prints class attribute