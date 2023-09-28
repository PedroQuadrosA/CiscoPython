my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]: # usamos um slice para ele começar a fazer a validação a partir do 1
    if i > largest:
        largest = i
print(largest)
