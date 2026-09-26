#Create a function smallest(a, b) that returns the smaller number
def smallest(a, b):
    if(a<b):
        return a
    return b
a = int(input())
b = int(input())
print(smallest(a, b))
