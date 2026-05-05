# 10) Find and print the product of all digits of a given number.

number = int(input("Enter a number : "))

product_result = 1

while number > 0:
    product_result *= number % 10
    number = number // 10

print(product_result)


## Optimized Solution

given_number = int(input("Enter a number : "))

result = 0 if given_number == 0 else 1

while given_number > 0:
    last_digit = given_number % 10

    if last_digit == 0:
        result = 0
        break

    result *= last_digit
    given_number //= 10

print(result)

