# 09 - Pyramid pattern.

for i in range(0, 5):
    for j in range(5 - i - 1):
        print("", end=" ")
    
    for k in range(i+1):
        print("*", end=" ")

    print()


# Another way

rows = 4

for i in range(1, rows + 1):
    print(" " * rows, end="")
    print("* " * i)

    rows -= 1