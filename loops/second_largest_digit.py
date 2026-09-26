#second largest digit
n = int(input())
large = -1
second_large = -1
while n>0:
    digit = n%10
    if digit> large:
        second_large = large
        large = digit
    elif digit >second_large and digit<large:
            second_large = digit
    n = n//10
print(second_large)
