# 23) Print all numbers between a and b divisible by 7.

a = int(input("Enter start number : "))

b = int(input("Enter End number : "))

while a <= b:
    if a %7 == 0:
        print(a)

    a += 1


## Optimized Solution

result_num = [i for i in range(a, b+1) if i % 7 == 0]

print(*result_num)