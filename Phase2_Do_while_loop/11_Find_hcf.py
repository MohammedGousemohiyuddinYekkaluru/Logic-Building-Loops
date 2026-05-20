# 11) Find HCF.

x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

if x<y:
    smaller = x

else:
    smaller = y

i = 1

while True:
    if (x % i == 0) and (y % i == 0):
        hcf = i

    i += 1

    if i == smaller:
        break

print(hcf)