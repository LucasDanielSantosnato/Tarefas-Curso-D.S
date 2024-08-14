# Função para contar a frequência de cada caractere em uma frase
def contar_caracteres(frase):
    # Cria um dicionário vazio para armazenar a contagem de caracteres
    contagem = {}

    # Itera sobre cada caractere na frase
    for caractere in frase:
        # Se o caractere já está no dicionário, incrementa sua contagem
        if caractere in contagem:
            contagem[caractere] += 1
        # Se o caractere não está no dicionário, adiciona-o com contagem 1
        else:
            contagem[caractere] = 1

    # Retorna o dicionário com a contagem de caracteres
    return contagem


# Lê a frase do usuário
frase = input("Digite uma frase: ")

# Chama a função e armazena o resultado
resultado = contar_caracteres(frase)

# Exibe o resultado
print("Contagem de caracteres:", resultado)
