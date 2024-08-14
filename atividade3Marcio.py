def soma_numeros_pares():
    soma = 0
    for num in range(50, 101, 2):
        soma += num
    return soma

resultado = soma_numeros_pares()
print("A soma dos números pares entre 50 e 100 é:", resultado)