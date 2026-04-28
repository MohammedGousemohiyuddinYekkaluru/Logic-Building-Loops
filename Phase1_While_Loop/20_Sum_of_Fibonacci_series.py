# 20) Find and print the sum of the Fibonacci series up to n terms.

n_terms = int(input("Enter a Number : "))

a = 0
b = 1

count = 0

sum_of_series = 0

while count < n_terms:
    sum_of_series += a

    a, b = b, a + b

    count += 1

print(sum_of_series)