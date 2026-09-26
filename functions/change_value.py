'''Create a function:
change_value()
There should be a global variable:
x = 10
The function should change x to 50 using global.'''
x = 10
def change_value():
    global x
    x = 50
    print(x)
change_value()
print(x)
