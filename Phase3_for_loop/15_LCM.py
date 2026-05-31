# 15) LCM

x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : "))

if x>y:
    greater = x

else:
    greater = y

while True:
    if (greater % x == 0) and (greater % y == 0):
        lcm = greater
        break

    greater += 1

print("LCM for {} & {} is {}".format(x,y,lcm))