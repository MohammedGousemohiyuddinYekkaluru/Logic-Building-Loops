# 14) Find and print the sum of digits of the given number.

number = int(input("Enter a number : "))

original_num = number

sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10
    number //= 10


print(f"The sum of digits of the given number {original_num} is {sum_of_digits}")