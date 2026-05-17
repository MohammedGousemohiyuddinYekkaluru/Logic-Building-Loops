# 3) Take input until 0 is entered and print sum.

result_sum = 0

while True:
    num = int(input("Enter a number : "))

    if num == 0:
        break

    result_sum += num

print("Sum =", result_sum)