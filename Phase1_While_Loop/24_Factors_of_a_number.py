# 24) Print all factors of the given number.

given_num = int(input("Enter a number of which you want the factors of : "))

start_num = 1

while start_num <= given_num:
    if given_num %start_num == 0:
        print(start_num)

    start_num += 1