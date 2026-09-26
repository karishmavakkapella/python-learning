'''Create a function is_positive(n) that checks whether
a number is positive, negative, or zero.'''
def is_positive(n):
    if(n>0):
        print("positive")
    elif(n<0):
        print("negative")
    else:
        print("zero")
n = int(input())
is_positive(n)
        
