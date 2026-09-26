'''Create a function count_digit(n, target)
that counts how many times target appears.'''
def count_digit(n, target):
    count =0
    while n>0:
        digit =n%10
        if(digit==target):
            count+=1
        n=n//10
    return count   
n = int(input())
target = int(input())
print(count_digit(n, target))
   
