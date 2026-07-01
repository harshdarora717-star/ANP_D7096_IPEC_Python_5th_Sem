#deletion from the list
my_list = [1,2,3,4,5,6,7,8,9,10]
index_to_delete = int(input("Enter the index of the element you want to delete: "))
del my_list[index_to_delete]  
print(my_list)