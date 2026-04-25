# 6) Calculate and print the sum of the first n natural numbers.

number = 5

original_number = number

total_sum = 0

while number > 0:
    total_sum += number

    number -= 1

print(f"The sum of {original_number} is {total_sum}")