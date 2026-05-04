# 7) Calculate the sum of all even numbers from 1 up to n.

original_n = 10

n = original_n

total_sum = 0

while n >= 1:
    if n % 2 == 0:
        total_sum += n
    
    n -= 1


print(total_sum)