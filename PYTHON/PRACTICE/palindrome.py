list_1 = [1,2,3,2,1]

list_2 = [1,3,5,6]

copy_list1 =list_1.copy()
copy_list1.reverse()

if(list_1==copy_list1):
  print("Palingdrome")

else:
  print("Not Palingdrome")
