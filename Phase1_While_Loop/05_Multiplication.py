# 5) Print the multiplication table of a given number from n x 1 to n x 10.


number = 5
i = 1

while i < 11:
    print(f"{number} x {i} = {number * i}")

    i += 1


## Optimized Solution

number = 6
limit = 10
i = 1

while i <= limit:
    print(f"{number} x {i} = {number * i}")

    i += 1