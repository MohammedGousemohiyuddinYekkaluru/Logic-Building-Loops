# 9) Calculate factorial.

original_n = int(input("Enter a number : "))

temp = original_n
fact = 1

while True:
    fact *= temp
    temp -= 1

    if temp == 0:
        break

print(fact)