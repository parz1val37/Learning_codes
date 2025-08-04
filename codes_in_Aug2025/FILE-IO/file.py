# t = "How are you!"

# f = open("nfile.txt", "w")  #using "w" mode to write on a file the already store data in file will be erased and new data will be written
# f.write(t)
# f.close() 

y = open("nfile.txt", "r")
l = y.readlines()   #filename.readlines() reads all the lines in a file and returns a list of lines
print(l, type(l))
y.close()

#------------------------------

k = open("nfile.txt")
x = k.readline()  # filename.readline() reads a single line from the file and returns it as a string
while x!= "":
    print(x, end="")
    x = k.readline()

k.close()