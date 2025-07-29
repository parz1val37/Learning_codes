#take user name and greets them according to day time
import datetime as dt
c = dt.datetime.now()
h = c.hour

x = input("Enter your name:")

if h >= 4 and h <= 11:
    print(f"Good morning, {x}!")
elif h >11 and h <= 16:
    print(f"good afternoon, {x}!")
elif h > 16 and h <= 20:
    print(f"Good evening, {x}!")
elif h > 20 or h < 4:
    print(f"Good night, {x}!")
else:
    print(f"Hello, {x}!")


