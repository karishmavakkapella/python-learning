#Create a function is_armstrong(n).
def is_armstrong(n):
    count = len(str(n))
    num = n
    total = 0
    while n>0:
        digit = n%10
        total+=digit**count
        n=n//10
    if(total==num):
        return True
    return False
    
n = int(input())
print(is_armstrong (n))
    
