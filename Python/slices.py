list_1 = [1]
list_2 = list_1 # aqui dizemos que a lista 2 sempre vai ser igual a 1
list_1[0] = 2
print(list_2)

list_3 = [1]
list_4 = list_3[:] # aqui copiamos a lista completamente
list_3[0] = 2
print(list_4)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # (3 - 1 = 2) aqueles indicies iguais a 1 e 2 mas nao o 3
print(new_list)

my_list2 = [10, 8, 6, 4, 2]
new_list2 = my_list2[1:-1]
print(new_list2)

my_list3 = [10, 8, 6, 4, 2]
new_list3 = my_list3[-1:1]
print(new_list3)

my_list4 = [10, 8, 6, 4, 2]
new_list4 = my_list4[:3] #equivalente a my_list[0:3]
print(new_list4)

my_list5 = [10, 8, 6, 4, 2]
new_list5 = my_list5[3:] #equivalente a my_list[start:len(my_list)]
print(new_list5)

my_list6 = [10, 8, 6, 4, 2]
del my_list6[:] #deleta tudo o que tem dentro da lista 
print(my_list6)
del my_list6 #DELETA A LISTA EM SI
