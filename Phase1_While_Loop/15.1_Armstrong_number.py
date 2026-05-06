# 15) Check whether the given number is an Armstrong number.

## Armstrong Number :- an integer that equals the sum of its own digits, each raised to the power of the total number of digits in the number.

original_num = 153

temp = original_num

total_sum = 0

while temp > 0:
    total_sum += (temp % 10) ** len(str(original_num))
    temp //= 10


if total_sum == original_num:
    print(f"Given number {original_num} is an Armstrong number")

else:
    print(f"Given number {original_num} is not an Armstrong number")


## Optimized Solution

### 1)

temp2 = original_num

no_of_digits = len(str(original_num))

sum2 = 0

while temp2 > 0:
    digit = temp2 % 10
    sum2 += digit ** no_of_digits
    temp2 //= 10

if sum2 == original_num:
    print(f"Given number {original_num} is an Armstrong number")

else:
    print(f"Given number {original_num} is not an Armstrong number")