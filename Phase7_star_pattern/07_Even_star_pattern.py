# 07 - Even star pattern (stars on even rows).

for i in range(0, 5):
    if not i % 2 == 0:
        for j in range(0, i+1):
            print("*", end= " ")
        
        print()
    else:
        print()    