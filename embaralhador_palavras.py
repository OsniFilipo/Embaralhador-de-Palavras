import random  # Importa o módulo random para embaralhar a lista de palavras

def embaralhar_palavras(lista_palavras):
    """
    Função para embaralhar uma lista de palavras.

    Argumentos:
    - lista_palavras: Uma lista de palavras a serem embaralhadas.

    Retorna:
    - Uma nova lista contendo as palavras embaralhadas.
    """
    random.shuffle(lista_palavras)  # Embaralha a lista de palavras
    return lista_palavras  # Retorna a lista de palavras embaralhadas

def main():
    """
    Função principal do programa.
    """
    palavras = input("Digite as palavras que deseja embaralhar, separadas por vírgula: ").split(",")  # Solicita ao usuário que digite as palavras a serem embaralhadas e as armazena em uma lista
    palavras_embaralhadas = embaralhar_palavras(palavras)  # Chama a função embaralhar_palavras para embaralhar a lista de palavras
    print("Palavras embaralhadas:", palavras_embaralhadas)  # Exibe a lista de palavras embaralhadas

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
