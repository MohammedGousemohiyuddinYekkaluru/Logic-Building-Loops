# 29) Find the largest digit in a number

original_number = int(input("Enter a number : "))

temp = abs(original_number)

largest_digit = 0

while temp > 0:
    last_digit = temp % 10

    if last_digit > largest_digit:
        largest_digit = last_digit

    if largest_digit == 9:
        break

    temp //= 10

print(f"The largest digit in your given number is {largest_digit}")