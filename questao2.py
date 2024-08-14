# Dicionário de exemplo
estoque = {
    "tomate": [1000, 2.30],  # [quantidade disponível, preço por unidade]
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}


# Função para encontrar o maior e o menor valor em um dicionário
def encontrar_maior_menor_valor(dicionario):
    # Verifica se o dicionário está vazio
    if not dicionario:
        return None, None

    # Inicializa as variáveis para armazenar o maior e o menor valor
    maior_valor = float('-inf')
    menor_valor = float('inf')

    # Itera sobre todos os valores do dicionário
    for chave, dados in dicionario.items():
        valor = dados[1]  # Estamos interessados no preço, que é o segundo item
        # Atualiza o maior valor encontrado
        if valor > maior_valor:
            maior_valor = valor
        # Atualiza o menor valor encontrado
        if valor < menor_valor:
            menor_valor = valor

    # Retorna o maior e o menor valor
    return maior_valor, menor_valor


# Chama a função e armazena o resultado
maior, menor = encontrar_maior_menor_valor(estoque)

# Exibe o resultado
print("Maior valor:", maior)
print("Menor valor:", menor)
