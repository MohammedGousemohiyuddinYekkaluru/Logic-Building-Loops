# 21) Print the square of each number from 1 to n.

n = int(input("Enter a number that how many squares you want : "))

start_num = 1

while start_num <= n:
    print(start_num ** 2)

    start_num += 1


## Optimized Solution

squares = [i ** 2 for i in range(1, n + 1)]

print(squares)