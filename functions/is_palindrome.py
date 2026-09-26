#Create a function is_palindrome(n).
def is_palindrome(n):
    num = n
    rev =0
    while(n>0):
        digit = n%10
        rev = rev*10+digit
        n = n//10
    if(num==rev):
        return True
    return False
n = int(input())
print(is_palindrome(n))
