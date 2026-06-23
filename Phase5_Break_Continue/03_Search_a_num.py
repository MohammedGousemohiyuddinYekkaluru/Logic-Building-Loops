# 03 - Search a number and break the loop when found.

search_num = int(input("Enter the search number: "))
start_num = 1

while search_num > 0:
    if search_num == start_num:
        print("number is found")
        break
    
    else:
        print(start_num)
        start_num += 1