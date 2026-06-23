# 04 - Stop when a negative number appears.

num = int(input("Enter a number : "))

while True:
    if num > 0:
        print(num)
        num = int(input("Enter a number : "))
    
    else:
        print("you entered -ve number")
        break