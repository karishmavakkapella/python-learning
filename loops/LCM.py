#lcm
a=int(input())
b=int(input())
while b>0:
    res=a%b
    a=b
    b =res
print(a)    
