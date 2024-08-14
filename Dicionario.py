#Aluno:Lucas Daniel Santos
#Turma:3 ano d

#aqui determina o dicionario, cria ele aqui.
estoque = {
    "tomate": [1000, 2.30],  # [quantidade disponível, preço por unidade]
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}

# Variável para armazenar o total de vendas.
total = 0

# Exibe o cabeçalho para a seção de vendas.
print("Vendas:\n")

# Inicia um loop infinito para registrar as vendas.
while True:
    # Solicita o nome do produto ao usuário.
    produto = input("Nome do produto (fim para sair) :")

    # Se o usuário digitar "fim", sai do loop.
    if produto == "fim":
        break

    # Verifica se o produto está no estoque.
    if produto in estoque:
        # Solicita a quantidade do produto ao usuário.
        quantidade = int(input("Quantidade:"))

        # Verifica se há quantidade suficiente do produto no estoque.
        if quantidade <= estoque[produto][0]:
            # Obtém o preço do produto.
            preco = estoque[produto][1]
            # Calcula o custo total da compra.
            custo = preco * quantidade
            # Exibe os detalhes da venda.
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            # Atualiza a quantidade no estoque.
            estoque[produto][0] -= quantidade
            # Adiciona o custo da venda ao total.
            total += custo
        else:
            # Mensagem de erro se a quantidade solicitada não estiver disponível.
            print("Quantidade solicitada não disponível")
    else:
        # Mensagem de erro se o nome do produto não for encontrado no estoque.
        print("Nome de produto inválido")

# Exibe o custo total das vendas após o término do loop.
print(f"\nCusto total: {total:21.2f}\n")

# Exibe o estoque atualizado.
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")

#professor: Carmona Costa.