a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if a<b:
    smaller = a

else:
    smaller = b

hcf_num = 0

for i in range(1, smaller + 1):
    if (a % i == 0) and (b % i == 0):
        hcf_num = i

print(hcf_num)