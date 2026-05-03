# 6) Calculate and print the sum of the first n natural numbers.

original_number = int(input("Enter a number : "))

temp = original_number

total_sum = 0

while temp > 0:
    total_sum += temp

    temp -= 1

print(f"The sum of {original_number} is {total_sum}")


## Optimized Solution

original_n_number = 10

temp = original_n_number

total_sum = original_n_number * (original_n_number + 1) // 2

print(f"The sum of first {original_n_number} natural numbers is {total_sum}")