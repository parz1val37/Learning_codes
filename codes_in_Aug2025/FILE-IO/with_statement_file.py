#With statement is very usefull for using files
#It automatically closes the file after the block of code is executed

with open('ofile.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a test file.\n')
# The file 'ofile.txt' is automatically closed after the with block
# No need to explicitly call file.close()

# Reading the file to verify content
with open('ofile.txt') as see:
    print(see.read())


