# 27) Find LCM of two numbers.

first_num = int(input("Enter first number : "))

second_num = int(input("Enter second number : "))

smallest_num = 0

largest_num = 0

hcf_num = 0

if first_num > second_num:
    largest_num = first_num
    smallest_num = second_num

else:
    smallest_num = first_num
    largest_num = second_num

while True:
    if largest_num %smallest_num == 0:
        hcf_num = smallest_num
        break

    else:
        largest_num, smallest_num = smallest_num, (largest_num %smallest_num)


lcm_num = (first_num * second_num) // hcf_num

print(f"the LCM of given two numbers {first_num}, {second_num} is {lcm_num}")