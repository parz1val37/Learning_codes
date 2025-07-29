def sqn(n):
    if(n < 0):
        return "incorrect input"
    elif(n==0):
        return 0
    else:
        return n + sqn(n-1)
    
a = sqn(int(input("enter no:")))
print(a)    