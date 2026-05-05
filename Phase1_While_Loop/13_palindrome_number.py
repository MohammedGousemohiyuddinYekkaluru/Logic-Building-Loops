# 13) Check whether the given number is a palindrome.

original_number = int(input("Enter a number : "))

temp = abs(original_number)

reverse_num = 0

while temp > 0:
    last_digit = temp % 10
    reverse_num = (reverse_num * 10) + last_digit
    
    temp //= 10

if original_number == reverse_num:
    print(f"Given Number {original_number} is a Palindrome")

else:
    print(f"Given Number {original_number} is not a Palindrome")


## Optimized Solution without using loops

s = str(original_number)

if s == s[::-1]:
    print("palindrome")

else:
    print("Not a Palindrome")