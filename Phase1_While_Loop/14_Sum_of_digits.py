# 14) Find and print the sum of digits of the given number.

original_num = int(input("Enter a number : "))

temp = original_num

sum_of_digits = 0

while temp > 0:
    sum_of_digits += temp % 10
    temp //= 10


print(f"The sum of digits of the given number {original_num} is {sum_of_digits}")


## Optimized Solution

temp2 = abs(original_num)

result_sum = 0

while temp2:
    result_sum += temp2 % 10
    result_sum //= 10

print(f"The sum of digits of the given number {original_num} is {result_sum}")