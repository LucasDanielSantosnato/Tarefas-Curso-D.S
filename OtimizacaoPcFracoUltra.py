import os


def criar_arquivos(pasta, num_arquivos):
    """Cria arquivos vazios dentro da pasta especificada."""
    for i in range(num_arquivos):
        arquivo_path = os.path.join(pasta, f"arquivo_{i}.txt")
        with open(arquivo_path, 'w') as f:
            pass  # Arquivo vazio


def criar_pastas_e_arquivos(diretorio, num_pastas, arquivos_por_pasta):
    """Cria pastas e arquivos desnecessários na área de trabalho."""
    for i in range(num_pastas):
        pasta = os.path.join(diretorio, f"pasta_{i}")
        os.makedirs(pasta, exist_ok=True)
        criar_arquivos(pasta, arquivos_por_pasta)


def main():
    # Define o caminho para a área de trabalho do usuário
    caminho_area_trabalho = os.path.join(os.path.expanduser("~"), "Desktop")

    # Define o número de pastas e arquivos por pasta
    num_pastas = 1000  # Número de pastas a serem criadas
    arquivos_por_pasta = 10  # Número de arquivos em cada pasta

    criar_pastas_e_arquivos(caminho_area_trabalho, num_pastas, arquivos_por_pasta)
    print("Pastas e arquivos criados com sucesso.")


if __name__ == "__main__":
    main()
