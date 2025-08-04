a = open("mfile.txt", "a")

text01 = "Have a nice day!\nWelcome to the world of Python."
a.write(text01)

text02 = "\nHow are you!\nThe End."   #.write() will overwrite the file and will add this text at the end
a.write(text02)

a.close()

