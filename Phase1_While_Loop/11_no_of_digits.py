# 11) Count and print the total number of digits in a given number.

number = int(input("Enter a number : "))

original_number = number

no_of_digits = 1 if number == 0 else 0 

while number > 0:
    no_of_digits += 1
    number //= 10


print(f"Number of digits in {original_number} is {no_of_digits} digits")