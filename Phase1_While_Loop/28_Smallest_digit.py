# 28) Find the smallest digit in a number

original_number = int(input("Enter a number : "))

temp = abs(original_number)


smallest_digit = 0 if temp == 0 else 9

while temp > 0:
    last_digit = temp % 10

    if last_digit < smallest_digit:
        smallest_digit = last_digit

    temp //= 10


print(f"smallest digit in the given number is {smallest_digit}")