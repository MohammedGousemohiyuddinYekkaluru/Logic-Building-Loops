# 08 - Odd star pattern (stars on odd rows).

for i in range(0, 5):
    if i % 2 == 0:
        for j in range(0, i+1):
            print("*", end=" ")
        
        print()
    
    else:
        print()