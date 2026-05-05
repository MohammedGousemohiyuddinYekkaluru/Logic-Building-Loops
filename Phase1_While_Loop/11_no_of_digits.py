# 11) Count and print the total number of digits in a given number.

original_number = int(input("Enter a number : "))

temp = original_number

no_of_digits = 1 if original_number == 0 else 0 

while temp > 0:
    no_of_digits += 1
    temp //= 10

print(f"Number of digits in {original_number} is {no_of_digits} digits")


## Optimized Solution without using loops

no_of_digits_2 = len(str(abs(original_number)))

print(no_of_digits_2)