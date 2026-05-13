# 4) Take input until 0 is entered and print the largest number.

largest_num = 0

while True:
    num = int(input("Enter a number : "))

    if num > largest_num:
        largest_num = num

    if num == 0:
        break

print(f"largest number = {largest_num}")