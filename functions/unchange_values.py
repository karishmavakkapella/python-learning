'''Create a function where a local variable x = 100 is created, while the
global variable x = 10 remains unchanged.'''
x =100
def unchange():
    x = 10
    print(x)
unchange()   
print(x)
