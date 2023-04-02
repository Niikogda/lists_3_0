
user_list=input("enter your list pls: ")

nums=0
lett=0
for i in user_list:
      if i.isalpha():
          lett+=1
      elif i.isnumeric():
          nums+=1
      
print("amount of letters= ", lett, "amount of numbers= ", nums)
print(user_list)
