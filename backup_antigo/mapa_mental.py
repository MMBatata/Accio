import json
import os

FICHEIRO = "mapa_mental.json"


def carregar():

    if os.path.exists(FICHEIRO):

        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)

    return {}


def guardar(mapa):

    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(mapa, f, indent=4, ensure_ascii=False)


def atualizar(divisao, objetos):

    mapa = carregar()

    if divisao not in mapa:
        mapa[divisao] = {}

    for objeto in objetos:

        if objeto not in mapa[divisao]:

            mapa[divisao][objeto] = {
                "vezes_visto": 1
            }

        else:

            mapa[divisao][objeto]["vezes_visto"] += 1

    guardar(mapa)


def mostrar():

    mapa = carregar()

    print("\n========== MAPA MENTAL ==========\n")

    for divisao, objetos in mapa.items():

        print(f"📍 {divisao}")

        for objeto, dados in objetos.items():

            print(f"   • {objeto} ({dados['vezes_visto']} vezes)")

        print()