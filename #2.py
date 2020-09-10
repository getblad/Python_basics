int_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 200]
sec_list = [el for el in int_list[1:] if el > int_list[int_list.index(el)-1]]
print(sec_list)