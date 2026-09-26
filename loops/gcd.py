a = int(input())
b = int(input())
multi = a*b
while b>0:
    gcd = a%b
    a=b
    b=gcd
res=multi//a
print(res)

