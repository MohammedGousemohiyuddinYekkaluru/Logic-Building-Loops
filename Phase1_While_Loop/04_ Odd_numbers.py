# 4) Print all odd numbers between 1 and 100

i = 1

while i < 101:
    if i %2 != 0:
        print(i)

    i += 1


## Optimized Solution

i = 1

while i <= 100:
    print(i)

    i += 2