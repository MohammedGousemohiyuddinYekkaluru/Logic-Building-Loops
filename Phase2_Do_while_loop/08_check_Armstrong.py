# 8) Check Armstrong number.

original_num = int(input("Enter a number : "))
temp = original_num
no_of_digits = len(str(original_num))

result_sum = 0

while True:
    result_sum += (temp % 10) ** no_of_digits
    temp //= 10

    if temp == 0:
        break

if original_num == result_sum:
    print(f"given number {original_num} is an Armstrong number.")

else:
    print(f"given number {original_num} is not an Armstrong number.")