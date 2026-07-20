import json
import os

FICHEIRO = "objetos.json"


def carregar():

    if not os.path.exists(FICHEIRO):
        return {}

    with open(FICHEIRO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar(memoria):

    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(memoria, f, indent=4, ensure_ascii=False)


def atualizar(objeto, divisao):

    memoria = carregar()

    memoria[objeto] = divisao

    guardar(memoria)


def onde_esta(objeto):

    memoria = carregar()

    return memoria.get(objeto)


def mostrar():

    memoria = carregar()

    print("\n===== MEMÓRIA VISUAL =====\n")

    for objeto, divisao in memoria.items():
        print(f"{objeto} -> {divisao}")