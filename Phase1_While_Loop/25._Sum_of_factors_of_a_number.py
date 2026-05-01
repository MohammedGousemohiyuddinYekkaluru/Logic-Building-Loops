# 25) Find the sum of all factors of the given number

given_num = int(input("Enter a number of which you want sum of factors : "))

start_num = 1

factors_sum = 0


while start_num <= given_num:
    if given_num %start_num == 0:
        factors_sum += start_num

    start_num += 1

print(f"Sum of all factors of the given number {given_num} is {factors_sum}")