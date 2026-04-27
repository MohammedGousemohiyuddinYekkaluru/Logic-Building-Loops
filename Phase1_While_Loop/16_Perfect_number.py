# 16) Check whether the given number is a Perfect number.

## Perfect Number :- is a positive integer that is equal to the sum of its proper divisors


number = int(input("Enter a number : "))

original_number = number

proper_divisors = []

while number > 0:
    if original_number %number == 0:
        proper_divisors.append(number)

    number -= 1

print(proper_divisors)

if sum(proper_divisors[1:]) == original_number:
    print(f"Given number {original_number} is a Perfect number")

else:
    print(f"Given number {original_number} is not a Perfect number")

