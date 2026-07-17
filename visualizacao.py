import os
import time

MAPA = [
    ["Sala", "Hall", "Cozinha"],
    ["", "Corredor", ""],
    ["Quarto1", "", "Quarto2"],
]


def mostrar_mapa(posicao):

    os.system("cls")

    print("\n===== MAPA DA CASA =====\n")

    for linha in MAPA:

        for divisao in linha:

            if divisao == "":
                print(" " * 15, end="")

            elif divisao == posicao:
                print(f"[🤖 {divisao:^8}]", end=" ")

            else:
                print(f"[   {divisao:^8}]", end=" ")

        print("\n")


    time.sleep(1.5)