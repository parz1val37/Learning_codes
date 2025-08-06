words = ["bad", "donkey"]

with open("words.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("words.txt", "w") as f:
    f.write(content)