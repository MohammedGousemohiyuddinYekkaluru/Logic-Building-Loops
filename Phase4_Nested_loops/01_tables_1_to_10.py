# 01 Print tables from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, (i * j)))