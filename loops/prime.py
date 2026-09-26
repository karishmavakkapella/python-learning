#Prime number
n = int(input("Enter a number:"))

if n < 2:
    print("not a prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("not a prime")
            break
    else:
        print("prime")
