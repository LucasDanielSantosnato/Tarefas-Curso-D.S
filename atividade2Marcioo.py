def separar_positivos_negativos(lista):
    positivos = []
    negativos = []

    for num in lista:
        if num >= 0:
            positivos.append(num)
        else:
            negativos.append(num)

    return positivos, negativos


# Exemplo de uso:
lista_numeros = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positivos, negativos = separar_positivos_negativos(lista_numeros)

print("Números positivos:", positivos)
print("Números negativos:", negativos)