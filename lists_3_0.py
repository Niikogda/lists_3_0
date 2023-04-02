
try:
  user_list=input("enter numbers for list with comma: ")
  list=[int(nums) for nums in user_list.split(",")]
  #list.append(user_list)
  list.reverse()
  print(list)
except:
  print("input numbers with comma")
finally:
        print ('done')
