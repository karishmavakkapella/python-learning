#smallest digit of a number
n = int(input("Enter a number:"))
n = abs(n)
small = 9
while n>0:
   if (n%10)<small:
        small = n%10
   n = n//10
print(small)
