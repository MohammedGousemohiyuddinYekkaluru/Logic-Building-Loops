# 13) Count positive numbers until a negative number is entered.

count_pos = 0

while True:
    ent_num = int(input("Enter a number : "))

    if ent_num < 0:
        break

    count_pos += 1

print(f"count of positive num is {count_pos}")