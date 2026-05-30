# 09) Sum of Fibonacci series.

a = 0
b = 1
n = int(input("Enter no.of series: "))

sum_of_series = 0

for i in range(1, n+1):
    print(a)
    sum_of_series += a

    a,b = b, a+b

print("Sum of fibonacci series is", sum_of_series)