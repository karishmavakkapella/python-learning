#Create a function largest(a, b) that returns the larger number.
def largest(a, b):
    if(a>b):
       return a
    return b
a = int(input())
b = int(input())
print(largest(a, b))
