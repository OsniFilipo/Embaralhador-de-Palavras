import random

def embaralhar_palavras(lista_palavras):
    random.shuffle(lista_palavras)
    return lista_palavras

def main():
    palavras = input("Digite as palavras que deseja embaralhar, separadas por vírgula: ").split(",")
    palavras_embaralhadas = embaralhar_palavras(palavras)
    print("Palavras embaralhadas:", palavras_embaralhadas)

if __name__ == "__main__":
    main()
