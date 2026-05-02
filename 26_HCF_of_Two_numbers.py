# 26) Find HCF of two numbers.

first_num = int(input("Enter first number : "))

second_num = int(input("Enter second number : "))

largest_num = 0

smallest_num = 0

Hcf_num = 0 

if first_num > second_num:
    largest_num = first_num
    smallest_num = second_num

else:
    largest_num = second_num
    smallest_num = first_num

while True:
    if largest_num %smallest_num == 0:
        Hcf_num = smallest_num
        break

    else:
        largest_num, smallest_num = smallest_num, (largest_num %smallest_num)

print(f"The HCF of given two numbers {first_num}, {second_num} is {Hcf_num}")

