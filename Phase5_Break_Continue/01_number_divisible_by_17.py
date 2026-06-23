# 01 - Stop loop when number divisible by 17 appears.

num = 2

while num > 0:
    if 17 % num == 0:
        break
    else:
        print(num)
        num += 1