# 2) Print multiplication table of a number.

num = int(input("Enter a number"))

i = 1

while True:
    if i <= 10:
        print(f"{num} * {i} = {num * i}")
        i += 1
    
    else:
        break