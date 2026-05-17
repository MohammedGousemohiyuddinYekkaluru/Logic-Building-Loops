# 5) Count digits in a number.

num = int(input("Enter a number : "))

temp = num

digits = 0

while True:
    digits += 1
    temp //= 10

    if temp == 0:
        break


print(f"no.of digits in {num} is {digits}")
