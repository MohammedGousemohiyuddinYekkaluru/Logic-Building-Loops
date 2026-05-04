# 7) Calculate the sum of all even numbers from 1 up to n.

# 1) Using while loop

original_num = int(input("Enter a number : "))

temp = original_num - 1 if original_num % 2 != 0 else original_num

total_sum = 0

while temp >= 1:
    total_sum += temp

    temp -= 2

print(f"The sum of Even numbers till {original_num} is {total_sum}")

# 2) Using math formula (without using while loop)

k = original_num // 2

result_sum = k * (k + 1)

print(f"The sum of Even numbers till {original_num} is {result_sum}")
