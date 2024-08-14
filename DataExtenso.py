from datetime import datetime
from num2words import num2words

# Lista para armazenar as datas convertidas
datas_convertidas = []

# Função para converter a data em formato por extenso
def data_por_extenso(data_str):
    try:
        # Convertendo a string da data para um objeto datetime
        data_obj = datetime.strptime(data_str, '%d/%m/%Y')

        # Formatando a data por extenso
        meses = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]

        dia = num2words(data_obj.day, lang='pt_BR')
        mes = meses[data_obj.month - 1]
        ano = num2words(data_obj.year, lang='pt_BR')

        return f'{dia} de {mes} de {ano}'
    except ValueError:
        return "Data inválida. Use o formato dd/mm/aaaa."

# Função para converter e armazenar uma data
def converter():
    data = input('Digite a data (dd/mm/aaaa): ')
    if data:
        data_extenso = data_por_extenso(data)
        datas_convertidas.append(data_extenso)
        print(f'Data por extenso: {data_extenso}')
    else:
        print("Entrada inválida. Tente novamente.")

# Função para listar todas as datas convertidas
def listar():
    if datas_convertidas:
        print("Datas convertidas:")
        for index, data in enumerate(datas_convertidas, start=1):
            print(f"{index}. {data}")
    else:
        print("Nenhuma data foi convertida ainda.")

# Função para encerrar o programa
def sair():
    print("Encerrando o programa.")
    exit()

# Função principal para o menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Converter Data")
        print("2. Listar Datas Convertidas")
        print("3. Sair")

        escolha = input("Escolha uma opção (1/2/3): ")

        if escolha == '1':
            converter()
        elif escolha == '2':
            listar()
        elif escolha == '3':
            sair()
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
Menu()
