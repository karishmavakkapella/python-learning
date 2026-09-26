#fibonacci series
n = int(input("Enter a number:"))
a = 0
b = 1

if n ==1:
    print("0")
elif n==0:
    print("no terms")
else:
            
    print(a,end=" ")
    print(b,end=" ")
    for i in range(3,n+1):
        c = a+b
        print(c,end =" ")
        a = b
       
        b = c
