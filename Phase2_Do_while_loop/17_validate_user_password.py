# 17) Validate user password with a retry limit.

user_email = input("enter email : ")
user_pass = int(input("enter password : "))

limit = 3
count = 0

while True:
    if user_email == "user@gmail.com" and user_pass == 1234:
        print("login successful")
        break

    elif user_email == "user@gmail.com" and user_pass != 1234:
        print("wrong password, Try again!")
        
        while count < limit:
            user_pass = int(input("enter password : "))
            count += 1

            if user_pass == 1234:
                print("Login successful")
                break
            else:
                print("Wrong again")
        
        if user_pass != 1234:
            print("Retry limit exceeded")
        
        break
    
    else:
        print("Wrong email and password")
        break