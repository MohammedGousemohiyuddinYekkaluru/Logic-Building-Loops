# 17) Sum of even numbers.

n_range = int(input("Enter range : "))

sum_of_even = 0

for i in range(0, n_range+1, 2):
    sum_of_even += i


print(sum_of_even)