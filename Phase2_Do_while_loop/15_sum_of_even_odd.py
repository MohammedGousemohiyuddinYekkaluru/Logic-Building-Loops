# 15) Find sum of even and odd digits separately.

or_num = int(input("Enter a number : "))
temp = or_num

even_sum = 0
odd_sum = 0

while True:
    last_digit = temp % 10
    if last_digit % 2 == 0:
        even_sum += last_digit
    
    else:
        odd_sum += last_digit
    
    temp //= 10

    if temp == 0:
        break

print(f"even sum = {even_sum}, odd sum = {odd_sum}")