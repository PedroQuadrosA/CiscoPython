steps = 0
c0 = int(input("Digite um numero: "))
while c0 <= 0:
    c0 = int(input("Digite um numero positivo e inteiro: "))
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("Total number of steps:", steps)
