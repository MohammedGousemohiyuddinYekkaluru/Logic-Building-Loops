# 7) Print primes between 1 to 100.
import math

for i in range(1, 101):
    is_prime = True

    if i == 2:
        is_prime = True
    
    elif i <= 1:
        is_prime = False
    
    elif i %2 == 0:
        is_prime = False

    elif i <= 100:
        divisor = 3
        limit = int(math.sqrt(i))

        if divisor <= limit:
            if i % divisor == 0:
                is_prime = False

    if is_prime:
        print(i)