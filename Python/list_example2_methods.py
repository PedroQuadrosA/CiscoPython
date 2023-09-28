numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4) # aqui adicionamos um numero no final da lista
print(len(numbers))
print(numbers)

numbers.insert(0,222) # aqui adicionamos um numero em qualquer luga da linha
                     # o primeiro quer dizer a posição que iremos inserir
                     # o segundo é o elemento que iremos inserir
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(len(numbers))
print(numbers)
print()

my_list = []
for i in range(5):
    my_list.append(i + 1)
print(my_list)

my_list2 = []
for i in range(5):
    my_list2.insert(0, i + 1) #aqui vai ser inverso do exemplo anterior
                              #pois ele sempre sera adicionado na primeira posição
print(my_list2)

my_list3 = [10, 1, 8, 3, 5]
print()
print(my_list3)
total = 0
for i in range(len(my_list3)): #o range vai ser o tamanho da lista
    total += my_list3[i] #aqui vamos pegar o numero que esta na posição i
                         # e adicionalo to total
print(total)
