# 10) Print Fibonacci series.

nth_term = 10

starting_n = 0
a = 0
b = 1

while True:
    print(a)

    a,b = b, a+b

    if starting_n == nth_term - 1:
        break

    starting_n += 1