#Create a function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n):
    if(n==1):
        print("0")
        return
    a = 0
    b = 1
    if(n==2):
        print(a,end = " ")
        print(b,end = " ")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(3,n+1):
            c = a+b
            a=b
            b=c
            print(c,end=" ")
n = int(input())
fibonacci(n)
