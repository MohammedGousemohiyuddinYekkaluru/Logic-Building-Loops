# 16) Check whether the given number is a Perfect number.

## Perfect Number :- is a positive integer that is equal to the sum of its proper divisors

original_num = int(input("Enter a number : "))

temp = original_num // 2

proper_divisors = []

while temp > 0:
    if original_num %temp == 0:
        proper_divisors.append(temp)

    temp -= 1

if sum(proper_divisors) == original_num:
    print(f"Given number {original_num} is a Perfect number")

else:
    print(f"Given number {original_num} is not a Perfect number")