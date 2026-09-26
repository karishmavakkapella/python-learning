#armstrong number
n = int(input("Enter a number:"))
num = n
total = 0
count = len(str(n))
while n>0:
    digit = n%10
    total +=digit**count
    n = n//10
    
if total == num:
    print("Armstrong number")
else:
    print("not an Armstrong number")
