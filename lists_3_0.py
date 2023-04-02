user_list=input("enter your list pls: ")
user_find=input('enter the symbol, you wanna find: ')
user_list.lower()
for i in user_list:
    x=user_find.count(user_list)
print(user_find, '=', x)
print(user_list)