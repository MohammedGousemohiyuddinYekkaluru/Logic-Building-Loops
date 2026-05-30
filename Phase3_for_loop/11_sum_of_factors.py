# 11) Sum of factors.

num = int(input("Enter a number : "))

sum_of_factors = 0

for i in range(1, num+1):
    if num % i == 0:
        sum_of_factors += i

print("sum of factors of number {} is {}".format(num, sum_of_factors))