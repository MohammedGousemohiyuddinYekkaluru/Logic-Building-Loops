# 10) Find and print the product of all digits of a given number.

number = int(input("Enter a number : "))

product_result = 1

while number > 0:
    product_result *= number % 10
    number = number // 10

print(product_result)



