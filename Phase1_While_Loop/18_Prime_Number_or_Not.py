# 18) Check whether the given number is a prime number.

given_number = int(input("Enter a number that you want to check : "))

divisor = 2

is_prime = True

while divisor < given_number:
    if given_number % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print(f"Given number {given_number} is a prime number")

else:
    print(f"Given number {given_number} is not a prime number")