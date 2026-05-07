# 17) Print all prime numbers between 1 and 100

import math

number = 2   # 2 is the only even prime number
print(number)

number = 3

while number <= 100:
    is_prime = True
    limit = int(math.sqrt(number))
    divisor = 3

    while divisor <= limit:
        if number % divisor == 0:
            is_prime = False
            break

        divisor += 2

    if is_prime:
        print(number)

    number += 2  # skipping even numbers because except 2 no even number is prime