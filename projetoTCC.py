import os
import platform
import ctypes
import sys
import time


def exibir_mensagem():
    # Define a mensagem a ser exibida
    mensagem = "Você foi traqueado, meu amigo!"

    # Determine o sistema operacional
    so = platform.system()

    if so == "Windows":
        # Use uma caixa de mensagem no Windows
        ctypes.windll.user32.MessageBoxW(0, mensagem, "Aviso", 1)
    elif so == "Linux" or so == "Darwin":
        # No Linux ou macOS, você pode usar o comando `zenity` ou `osascript` para exibir uma caixa de mensagem
        os.system(f"zenity --info --text='{mensagem}'")
    else:
        print(mensagem)


def reiniciar_pc():
    # Determine o sistema operacional e execute o comando de reinício apropriado
    so = platform.system()

    if so == "Windows":
        os.system("shutdown /r /t 0")
    elif so == "Linux":
        os.system("sudo reboot")
    elif so == "Darwin":
        os.system("sudo shutdown -r now")
    else:
        print("Sistema operacional não suportado para reinício automático.")


def main():
    exibir_mensagem()
    # Adicione um pequeno atraso para garantir que a mensagem seja exibida antes do reinício
    time.sleep(5)
    reiniciar_pc()


if __name__ == "__main__":
    main()
