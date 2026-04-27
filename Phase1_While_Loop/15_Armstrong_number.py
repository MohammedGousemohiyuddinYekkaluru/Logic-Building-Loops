# 15) Check whether the given number is an Armstrong number.

## Armstrong Number :- an integer that equals the sum of its own digits, each raised to the power of the total number of digits in the number.

number = int(input("Enter a Number : "))

original_number = number

temp = number

no_of_digits = 1 if number == 0 else 0

total_sum = 0

# Solving it using two loops

while number > 0:
    no_of_digits += 1
    number //= 10


while temp > 0:
    total_sum += (temp % 10) ** no_of_digits
    temp //= 10

if total_sum == original_number:
    print(f"Given number {original_number} is an Armstrong number")

else:
    print(f"Given number {original_number} is not an Armstrong number")