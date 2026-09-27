import json
import os

FICHEIRO = "cerebro.json"


def carregar():

    if os.path.exists(FICHEIRO):

        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "robot": {
            "x": 0,
            "y": 0,
            "divisao": "Hall de entrada"
        },

        "objetos": {},

        "divisoes": {}
    }


def guardar(cerebro):

    with open(FICHEIRO, "w", encoding="utf-8") as f:

        json.dump(cerebro, f, indent=4, ensure_ascii=False)


def atualizar_objeto(nome, divisao):

    cerebro = carregar()

    if nome not in cerebro["objetos"]:

        cerebro["objetos"][nome] = {

            "divisao": divisao,

            "x": 0,

            "y": 0,

            "chip": None,

            "ultima_vez_visto": 0

        }

    else:

        cerebro["objetos"][nome]["divisao"] = divisao

    guardar(cerebro)

def mostrar():

    cerebro = carregar()

    print("\n========== CÉREBRO ==========\n")

    print("🤖 Robô")

    print(cerebro["robot"])

    print()

    print("📦 Objetos")

    for objeto in cerebro["objetos"]:

        print(objeto)

        print(cerebro["objetos"][objeto])

        print()