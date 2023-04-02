
user_list=input("enter your list pls: ")
list=[]
list.append(user_list) 
nums=0
lett=0
for i in list:
    if i.isalpha():
        lett+=1
    elif i.isnumeric():
        nums+=1
    else:
        lett+=0
        nums+=0
print("amount of letters= ", lett, "amount of numbers= ", nums)
print(list)