# 19) Print the Fibonacci series up to n terms.


starting_num = 0

nth_term = 10

first_term = 0

second_term = 1

while starting_num < nth_term:
    print(first_term)

    first_term, second_term = second_term, first_term + second_term

    starting_num += 1