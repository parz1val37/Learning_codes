print("ENTER DIMENSIONS OF RECTANGLE:")

a = int(input("enter length:"))
b = int(input("enter width:"))  

def area(c,d):
    if(c < 0 or d < 0):
        print('incorrect data')
    else:
         area = c*d
         print(f"length is {a} width is {b} \nAREA:{area}")
    
area(a,b)
