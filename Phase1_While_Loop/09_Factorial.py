# 9) Calculate and print the factorial of a given number.


given_number = int(input("Enter a number : "))

factorial = 1

while given_number > 0:
    factorial *= given_number

    given_number -= 1


print(factorial)