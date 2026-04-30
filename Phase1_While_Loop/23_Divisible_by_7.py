# 23) Print all numbers between a and b divisible by 7.

a = int(input("Enter start number : "))

b = int(input("Enter End number : "))

while a <= b:
    if a %7 == 0:
        print(a)

    a += 1