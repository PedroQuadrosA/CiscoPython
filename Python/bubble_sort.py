my_list = [8, 10, 6, 2, 4]
my_list2 = [9, 11, 7, 5, 1]
print(my_list2)
print(my_list)
swapped = True

while swapped:
    swapped = False # no swaps so far
    for i in range(len(my_list) - 1): #(5 - 1)
        if my_list[i] > my_list[i + 1]:
            swapped = True # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    for i in range(len(my_list2) - 1): #(5 - 1)
        if my_list2[i] < my_list2[i + 1]:
            swapped = True # a swap occurred!
            my_list2[i], my_list2[i + 1] = my_list2[i + 1], my_list2[i]
    
print(my_list)
print(my_list2)
