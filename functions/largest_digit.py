#Create a function largest_digit(n).
def  largest_digit(n):
    large = -1
    while n>0:
        digit = n%10
        if digit>large:
            large = digit
        n = n//10
    return large
n = int(input())
print(largest_digit(n))
        
        
    
