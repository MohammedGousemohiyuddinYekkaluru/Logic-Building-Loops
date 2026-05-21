# 14) Find sum of digits.

original_num = int(input("Enter a number : "))
temp = original_num

result_sum = 0

while True:
    result_sum += temp % 10
    temp //= 10

    if temp == 0:
        break

print(f"The sum of digits of {original_num} is {result_sum}")