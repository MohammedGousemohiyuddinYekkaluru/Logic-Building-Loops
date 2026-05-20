# 12) Create a menu-driven program.

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
        num1 = int(input("Enter num 1 : "))
        num2 = int(input("Enter num 2 : "))
        print(f"addition of {num1}, {num2} is {num1 + num2}")

    elif user_selection == 2:
        num1 = int(input("Enter num 1 : "))
        num2 = int(input("Enter num 2 : "))
        print(f"subtrcation of {num1}, {num2} is {num1 - num2}")
    
    elif user_selection == 3:
        num1 = int(input("Enter num 1 : "))
        num2 = int(input("Enter num 2 : "))
        print(f"product of {num1}, {num2} is {num1 * num2}")
    
    elif user_selection == 4:
        num1 = int(input("Enter num 1 : "))
        num2 = int(input("Enter num 2 : "))
        print(f"division of {num1}, {num2} is {num1 / num2}")
    
    elif user_selection == 5:
        print("Exiting the program")
        break

    else:
        print("Select a correct option")