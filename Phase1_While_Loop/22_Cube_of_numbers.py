# 22) Print the cube of each number from 1 to n.

n_numbers = int(input("Enter a number that how many cubes you want : "))

start_num = 1

while start_num <= n_numbers:
    print(start_num ** 3)

    start_num += 1