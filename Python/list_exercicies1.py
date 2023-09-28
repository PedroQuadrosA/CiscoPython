hat_list = [1, 2, 3, 4, 5] # minha lista de numeros escondidos
print(hat_list)
number = int(input("Digite um numero para substituir o numero do meio da lista: "))
hat_list[2] = number
print(hat_list)
del hat_list[4]
print(hat_list)
print("The list's length:", len(hat_list))
