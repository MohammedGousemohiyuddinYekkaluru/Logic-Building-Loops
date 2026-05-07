# Check whether the given number is a prime number.
import math

given_number = int(input("Enter a number that you want to check : "))

if given_number < 2:
    is_prime = False

elif given_number == 2:
    is_prime = True

elif given_number %2 == 0:
    is_prime = False

else:
    is_prime = True
    limit = int(math.sqrt(given_number))
    divisor = 3

    while divisor <= limit:
        if given_number % divisor == 0:
            is_prime = False
            break

        divisor += 2


if is_prime:
    print(f"Given number {given_number} is a prime number")

else:
    print(f"Given number {given_number} is not a prime number")

