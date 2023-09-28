#trocando valor de uma variavel

variable_1 = 1
variable_2 = 2
variable_3 = 3
variable_4 = 4
aux = 0
print(variable_1)
print(variable_2)
print(variable_3)
print(variable_4)

aux = variable_1
variable_1 = variable_2
variable_2 = aux
print("Usando uma variavel auxiliar para trocar os valores")
print("Novo valor da variavel 1:", variable_1)
print("Novo valor da variavel 2:", variable_2)
print()

variable_3, variable_4 = variable_4, variable_3
print("Usando uma forma oferecida pelo Python")
print("Novo valor da variavel 3:", variable_3)
print("Novo valor da variavel 4:", variable_4)


