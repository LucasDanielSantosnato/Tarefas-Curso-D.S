def calcular_moda(lista):
    frequencias = {}
    for elemento in lista:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1

    maior_frequencia = 0
    moda = []

    for elemento, frequencia in frequencias.items():
        if frequencia > maior_frequencia:
            maior_frequencia = frequencia
            moda = [elemento]
        elif frequencia == maior_frequencia:
            moda.append(elemento)

    return moda, maior_frequencia


def main():
    # Entrada dos dados
    lista = []
    for i in range(10):
        try:
            elem = int(input("Digite um elemento da lista: "))
            lista.append(elem)
        except ValueError:
            print("Por favor, digite um número inteiro.")
            continue

    print("Lista:", lista)

    # Resultados
    moda, frequencia = calcular_moda(lista)
    print("Moda:", moda)
    print("Frequência:", frequencia)


if __name__ == "__main__":
    main()
