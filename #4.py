list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [x for x in list if list.count(x) == 1]
print(new_list)