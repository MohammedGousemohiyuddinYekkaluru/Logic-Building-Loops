# 13) Check whether the given number is a palindrome.

number = int(input("Enter a number : "))

original_number = number

reverse_num = 0

while number > 0:
    last_digit = number % 10
    reverse_num = (reverse_num * 10) + last_digit
    
    number //= 10

if original_number == reverse_num:
    print(f"Given Number {original_number} is a Palindrome")

else:
    print(f"Given Number {original_number} is not a Palindrome")