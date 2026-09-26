#Create a function count_digits(n)
def count_digits(n):
    count = 0
    if n==0:
        return 1
    while n>0:
       count+=1
       n= n//10
    return count
n = int(input())
print(count_digits(n))
