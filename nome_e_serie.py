# Função para capturar o nome e a série do usuário
def capturar_dados():
    # Solicita que o usuário digite seu nome
    nome = input("Digite seu nome: ")

    # Solicita que o usuário digite sua série
    serie = input("Digite sua série: ")

# Função que recebe o nome e a série e imprime uma mensagem formatada
def imprimir_dados(nome, serie):
    # Exibe uma mensagem personalizada com os dados fornecidos
    print(f"Olá {nome}, sua série é a {serie}")

# Função principal que orquestra o funcionamento do programa
def main():
    # Chama a função para capturar dados e armazena os retornos em duas variáveis
    nome, serie = capturar_dados()

    # CHama a função para imprimir os dados recebidos
    imprimir_dados(nome, serie)

# Verifica se o arquivo está sendo executado diretamente (e não importado)
if __name__ == "__main__":
    # Executa a função principal
    main()
