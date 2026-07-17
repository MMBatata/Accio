import json
import os
from datetime import datetime

FICHEIRO = "memoria_visual.json"


def carregar():

    if os.path.exists(FICHEIRO):

        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)

    return {}


def guardar(memoria):

    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(memoria, f, indent=4, ensure_ascii=False)


def atualizar(objetos, divisao):

    memoria = carregar()

    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    for objeto in objetos:

        memoria[objeto] = {
            "divisao": divisao,
            "ultima_vista": agora
        }

    guardar(memoria)


def mostrar():

    memoria = carregar()

    print("\n====== MEMÓRIA VISUAL ======\n")

    if len(memoria) == 0:

        print("Ainda não existe informação.")

    else:

        for objeto, dados in memoria.items():

            print(
                f"{objeto} → {dados['divisao']} ({dados['ultima_vista']})"
            )

    print()