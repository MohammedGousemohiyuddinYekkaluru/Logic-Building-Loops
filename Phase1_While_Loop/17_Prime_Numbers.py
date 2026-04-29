# 17) Print all prime numbers between 1 and 100

number = 2

while number <= 100:
    is_prime = True

    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            is_prime = False
            break

        divisor += 1

    if (is_prime):
        print(number)

    number += 1
