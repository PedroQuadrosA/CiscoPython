secret_word = input("Digite a palavra secreta: ")

while secret_word != 'chupacabra':
    if secret_word == 'chupacabra':
        break
    else:
        print("Palavra secreta errada, tente de novo.")
        secret_word = input("Digite a palavra secreta: ")
print("Acesso permitido.")
