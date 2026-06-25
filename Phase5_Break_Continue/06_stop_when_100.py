# 06 - Stop when the running sum exceeds 100.

r_sum = 0

while True:

    if r_sum > 100:
        break

    else:
        num = int(input("Enter a number: "))
        r_sum += num
        print(r_sum)