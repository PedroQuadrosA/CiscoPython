my_list = [10, 1, 8, 3, 5]
print(my_list)
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)
print("Usando o for para inverter a sua ordem")
my_list2 =[1, 2, 3, 4, 5]
lenght = len(my_list2)
print(my_list2)
for i in range(lenght // 2):
    my_list2[i], my_list2[lenght - i - 1] = my_list2[lenght - i - 1], my_list2[i]
    print(my_list2)
