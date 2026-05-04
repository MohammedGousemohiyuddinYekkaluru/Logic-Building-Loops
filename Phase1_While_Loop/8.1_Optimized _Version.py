# 8) Calculate the sum of all odd numbers from 1 up to n.

# 1) using while loop

original_num = int(input("Enter a number : "))

temp = original_num - 1 if original_num % 2 == 0 else original_num

total_sum = 0

while temp >= 1:
    total_sum += temp

    temp -= 2

print(f"The sum of odd numbers till {original_num} is {total_sum}")

# 2) Using math formula (without using loop)

n = (original_num + 1) // 2

result_sum = n ** 2

print(f"The sum of odd numbers till {original_num} is {result_sum}")