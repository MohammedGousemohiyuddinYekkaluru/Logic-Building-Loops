# 03 Count factors for each number in a range.

count = 0

for i in range(5, 11):
    for j in range(1, i):
        if i % j == 0:
            print(i)
            count += i

print(count)