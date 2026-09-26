#sum of even numbers upto n
n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    if i%2==0:
       sum+=i
print(f"sum of  even numbers(1 to {n}) is:",sum)
