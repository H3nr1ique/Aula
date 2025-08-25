def criar_tabuada(numero):
    print(f"Tabuada do {numero}:")

    for i in range(1 ,11):
        print(f"{numero} x {i} = {numero * i}")

# Pedir o número ao usuário
numero = int(input("Digite o número para a tabuada: "))

# Criar a tabuada
criar_tabuada(numero)