# 7) Check palindromes.

text = input("Enter a string : ")
temp = text

reverse_str = ""

while True:
    reverse_str += temp[-1]
    temp = temp[:-1]

    if temp == "":
        break

if text == reverse_str:
    print(f"{text} is a palindrome.")

else:
    print(f"{text} is not a palindrome.")