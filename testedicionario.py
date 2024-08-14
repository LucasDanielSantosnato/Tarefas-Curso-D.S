import tkinter as tk

# Função para exibir a tela de vendas
def mostrar_vendas():
    global total
    produto = produto_entry.get()
    if produto == "fim":
        resultado_text.set(f"\nCusto total: {total:.2f}\n")
        estoque_text.set("")
        return

    if produto in estoque:
        try:
            quantidade = int(quantidade_entry.get())
            if quantidade <= estoque[produto][0]:
                preco = estoque[produto][1]
                custo = preco * quantidade
                resultado_text.set(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
                estoque[produto][0] -= quantidade
                total += custo
            else:
                resultado_text.set("Quantidade solicitada não disponível")
        except ValueError:
            resultado_text.set("Quantidade inválida")
    else:
        resultado_text.set("Nome de produto inválido")

    # Atualiza o estoque na tela
    estoque_str = "\n".join(f"Descrição: {chave}\nQuantidade: {dados[0]}\nPreço: {dados[1]:6.2f}\n" for chave, dados in estoque.items())
    estoque_text.set(estoque_str)

# Configuração do estoque
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}

total = 0

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sistema de Vendas")

# Configuração da cor de fundo verde
root.configure(bg='green')

# Criação dos widgets
tk.Label(root, text="Nome do produto:", bg='green', fg='white').pack()
produto_entry = tk.Entry(root)
produto_entry.pack()

tk.Label(root, text="Quantidade:", bg='green', fg='white').pack()
quantidade_entry = tk.Entry(root)
quantidade_entry.pack()

tk.Button(root, text="Registrar Venda", command=mostrar_vendas).pack()

resultado_text = tk.StringVar()
tk.Label(root, textvariable=resultado_text, bg='green', fg='white').pack()

estoque_text = tk.StringVar()
tk.Label(root, textvariable=estoque_text, bg='green', fg='white').pack()

root.mainloop()
