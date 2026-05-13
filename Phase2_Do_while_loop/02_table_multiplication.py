# 2) Print multiplication table of a number.

num = int(input("Enter a number"))

i = 1

while True:
    if i <= 10:
        print(f"{num} * {i} = {num * i}")
        i += 1
    
    else:
        break


## Proper do-while loop logic

num = int(input("Enter a number"))

i = 1

while True:
    print(f"{num} * {i} = {num * i}")
    i += 1

    if i > 10:
        break