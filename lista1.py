import os

# Lista que armazena a agenda de contatos
agenda = []
# Variável para marcar se houve uma alteração na agenda
alterada = False

# Função para pedir o nome do usuário
def pede_nome(padrao=""):
    """Solicita um nome ao usuário. Se não for fornecido, utiliza o valor padrão."""
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
    return nome

# Função para pedir o telefone do usuário
def pede_telefone(padrao=""):
    """Solicita um telefone ao usuário. Se não for fornecido, utiliza o valor padrão."""
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
    return telefone

# Função para pedir o endereço do usuário
def pede_endereco(padrao=""):
    """Solicita um endereço ao usuário. Se não for fornecido, utiliza o valor padrão."""
    endereco = input("Endereço: ")
    if endereco == "":
        endereco = padrao
    return endereco

# Função para pedir a cidade do usuário
def pede_cidade(padrao=""):
    """Solicita uma cidade ao usuário. Se não for fornecida, utiliza o valor padrão."""
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrao
    return cidade

# Função para pedir o campo adicional VF ao usuário
def pede_vf(padrao=""):
    """Solicita o campo adicional VF ao usuário. Se não for fornecido, utiliza o valor padrão."""
    vf = input("VF: ")
    if vf == "":
        vf = padrao
    return vf

# Função para exibir os dados de um contato
def mostra_dados(nome, telefone, endereco, cidade, vf):
    """Exibe os dados do contato."""
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereco} Cidade: {cidade} VF: {vf}")

# Função para pedir o nome do arquivo ao usuário
def pede_nome_arquivo():
    """Solicita o nome do arquivo ao usuário."""
    return input("Nome do arquivo: ")

# Função para pesquisar um contato pelo nome na agenda
def pesquisa(nome):
    """Busca um contato pelo nome e retorna o índice se encontrado, ou None se não encontrado."""
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

# Função para verificar se o nome já está na agenda
def verifica_repeticao(nome):
    """Verifica se o nome já existe na agenda e retorna True se existir, caso contrário, False."""
    if pesquisa(nome) is not None:
        print("Erro: O nome já está na agenda.")
        return True
    return False

# Função para adicionar um novo contato à agenda
def novo():
    """Adiciona um novo contato à agenda e marca que houve uma alteração."""
    global agenda, alterada
    nome = pede_nome()
    if verifica_repeticao(nome):
        return  # Não adiciona se o nome já estiver na agenda
    telefone = pede_telefone()
    endereco = pede_endereco()
    cidade = pede_cidade()
    vf = pede_vf()
    agenda.append([nome, telefone, endereco, cidade, vf])
    alterada = True

# Função para confirmar uma operação com o usuário
def confirma(operação):
    """Solicita confirmação do usuário para uma operação e retorna True para sim e False para não."""
    while True:
        opção = input(f"Confirma {operação}? (S/N): ").upper()
        if opção in "SN":
            return opção == "S"
        print("Resposta inválida. Escolha S ou N.")

# Função para apagar um contato da agenda
def apaga():
    """Apaga um contato da agenda, se encontrado, e marca que houve uma alteração."""
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento"):
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

# Função para alterar um contato existente na agenda
def altera():
    """Altera um contato existente na agenda, se encontrado, e marca que houve uma alteração."""
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome, telefone, endereco, cidade, vf = agenda[p]
        print("Encontrado:")
        mostra_dados(nome, telefone, endereco, cidade, vf)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor
        telefone = pede_telefone(telefone)
        endereco = pede_endereco(endereco)
        cidade = pede_cidade(cidade)
        vf = pede_vf(vf)
        if confirma("alteração"):
            agenda[p] = [nome, telefone, endereco, cidade, vf]
            alterada = True
    else:
        print("Nome não encontrado.")

# Função para listar todos os contatos na agenda
def lista():
    """Lista todos os contatos na agenda."""
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")

# Função para ler a última agenda gravada
def lê_última_agenda_gravada():
    """Lê e carrega a última agenda gravada, se disponível."""
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

# Função para obter o nome do último arquivo de agenda gravado
def última_agenda():
    """Retorna o nome do último arquivo de agenda gravado."""
    try:
        with open("ultima_agenda.dat", "r", encoding="utf-8") as arquivo:
            última = arquivo.readline().strip()
    except FileNotFoundError:
        return None
    return última

# Função para atualizar o nome do último arquivo de agenda gravado
def atualiza_última(nome):
    """Atualiza o arquivo com o nome da última agenda gravada."""
    with open("ultima_agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

# Função para ler a agenda a partir de um arquivo
def leia_arquivo(nome_arquivo):
    """Lê a agenda a partir de um arquivo e atualiza a agenda global."""
    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone, endereco, cidade, vf = l.strip().split("#")
            agenda.append([nome, telefone, endereco, cidade, vf])
    alterada = False

# Função para ler a agenda e, se alterada, perguntar se deseja salvar
def lê():
    """Lê a agenda a partir de um arquivo e, se houver alterações não salvas, pergunta se deseja salvar."""
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação"):
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)

# Função para ordenar a agenda por nome
def ordena():
    """Ordena a agenda por nome usando o método de ordenação por bolha (bubble sort)."""
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i][0].lower() > agenda[i + 1][0].lower():
                # Troca os elementos
                agenda[i], agenda[i + 1] = agenda[i + 1], agenda[i]
                trocou = True
            i += 1
        if not trocou:
            break
    alterada = True

# Função para gravar a agenda em um arquivo
def grava():
    """Grava a agenda em um arquivo e atualiza o nome do último arquivo gravado."""
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
    atualiza_última(nome_arquivo)
    alterada = False

# Função para validar se o valor inserido está dentro do intervalo permitido
def valida_faixa_inteiro(pergunta, inicio, fim):
    """Solicita um valor inteiro ao usuário dentro de um intervalo específico."""
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

# Função para exibir o menu de opções e processar a escolha do usuário
def menu():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para melhor visualização
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nContatos na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

# Função principal
if __name__ == "__main__":
    lê_última_agenda_gravada()
    while True:
        opção = menu()
        if opção == 0:
            break
        elif opção == 1:
            novo()
        elif opção == 2:
            altera()
        elif opção == 3:
            apaga()
        elif opção == 4:
            lista()
        elif opção == 5:
            grava()
        elif opção == 6:
            lê()
        elif opção == 7:
            ordena()
