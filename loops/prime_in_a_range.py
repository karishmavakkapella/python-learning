#prime number in a range
print("Enter two numbers:")
n1= int(input())
n2=int(input())
for n in range(n1,n2+1):
    if n<2:
     print(n,"not a prime")
    elif n==2:
     print(n,"prime ")
    else:
     for i in range(2,int(n**0.5)+1) :
        if n%i==0:
          print(n,"not a prime")
          break
     else:
        print(n,"prime")
