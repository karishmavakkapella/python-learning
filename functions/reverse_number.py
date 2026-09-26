#Create a function reverse_number(n).
def reverse_number(n):
    rev = 0
    while(n>0):
        digit = n%10
        rev = rev*10+digit
        n = n//10
    return  rev
n=int(input())
print(reverse_number(n))
                            
