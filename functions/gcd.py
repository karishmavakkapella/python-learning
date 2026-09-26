#Create a function gcd(a, b).
def gcd(a, b):
    while b>0:
        res = a%b
        a=b
        b=res
    return a
a = int(input())
b = int(input())
print(gcd(a, b))
