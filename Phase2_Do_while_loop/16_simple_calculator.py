# 16) Implement a simple calculator using a menu.
num1 = int(input("Enter 1st num : "))
num2 = int(input("Enter 2nd num : "))

while True:
    print("""
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit
        """)
    user_selection = int(input("select an option from above(in number) : "))

    if user_selection == 1:
        print(f"addition of {num1}, {num2} is {num1 + num2}")
    
    elif user_selection == 2:
        print(f"subtraction of {num1}, {num2} is {num1 - num2}")

    elif user_selection == 3:
        print(f"multiplication of {num1}, {num2} is {num1 * num2}")
    
    elif user_selection == 4:
        print(f"division of {num1}, {num2} is {num1 / num2}")
    
    elif user_selection == 5:
        print("Exiting the program")
        break

    else:
        print("Enter a valid option")