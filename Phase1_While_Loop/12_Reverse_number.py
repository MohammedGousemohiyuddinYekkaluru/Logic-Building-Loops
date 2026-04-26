# 12) Reverse the given number and print the reversed value

number = int(input("Enter a number : "))

original_number = number

reverse_num = 0

while number > 0:
    last_digit = number % 10
    reverse_num = (reverse_num * 10) + last_digit
    
    number //= 10

print(reverse_num)