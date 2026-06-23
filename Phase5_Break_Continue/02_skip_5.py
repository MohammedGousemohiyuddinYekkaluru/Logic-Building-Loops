# 02 - Skip numbers divisible by 5.

for i in range(30, 91):
    if i % 5 == 0:
        continue
    else:
        print(i)