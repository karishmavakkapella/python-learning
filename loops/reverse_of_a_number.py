#rev a number 
n = int(input())
num =n
rev = 0
while n!=0:
    digit= n%10
    rev = rev*10+digit
    n = n//10
print(f"reverse of {num} is :{rev}")
