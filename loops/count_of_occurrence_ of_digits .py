# count of occurrence of digits 
n = int(input())
num = str(n)
for i in range(len(num)):
    digit = num[i]
    found = False
    for j in range(i):
        if num[j]==digit:
           found = True 
           break;
    if(not found):
       print(digit,"-",num.count(digit))
