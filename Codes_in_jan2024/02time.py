import time
Time = int(time.strftime("%H"))
a = (input("Your name:"))
if(Time >= 0 and Time <= 6):
 print("Have a good sleep",a)
elif(Time > 6 and Time <= 12):
 print("Good Morning",a)
elif(Time >12 and Time <=18):
 print("Good Evening",a)
elif(Time >18 and Time <= 23):
 print("See you later",a)
else:
 print("time error")