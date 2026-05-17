# 6) Reverse a number.

num = int(input("Enter a number : "))

temp = num

reverse_num = 0

while True:
    last_digit = temp % 10
    reverse_num = (reverse_num * 10) + last_digit
    temp //= 10

    if temp == 0:
        break

print(reverse_num)