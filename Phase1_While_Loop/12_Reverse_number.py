# 12) Reverse the given number and print the reversed value

original_number = int(input("Enter a number : "))

temp = abs(original_number)

reverse_num = 0

while temp > 0:
    last_digit = temp % 10
    reverse_num = (reverse_num * 10) + last_digit
    
    temp //= 10

if original_number < 0:
    reverse_num *= -1

print(reverse_num)


## Optimized Version without using loops

reversed_num = int(str(abs(original_number)) [::-1])

if original_number < 0:
    reversed_num *= -1

print(reversed_num)