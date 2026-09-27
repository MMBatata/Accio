import json
import os
from datetime import datetime

FICHEIRO_ROTINAS = "rotinas.json"
FICHEIRO_CASA = "casa.json"
FICHEIRO_OBJETOS = "objetos.json"


# ---------------- ROTINAS ---------------- #

def carregar_rotinas():

    if os.path.exists(FICHEIRO_ROTINAS):

        with open(FICHEIRO_ROTINAS, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "rotinas": [
            {
                "nome": "Ronda do meio-dia",
                "hora": "12:00",
                "acao": "ronda"
            },
            {
                "nome": "Ronda noturna",
                "hora": "22:30",
                "acao": "ronda"
            }
        ]
    }


def guardar_rotinas(rotinas):

    with open(FICHEIRO_ROTINAS, "w", encoding="utf-8") as f:
        json.dump(rotinas, f, indent=4, ensure_ascii=False)


def criar_ficheiro():

    if not os.path.exists(FICHEIRO_ROTINAS):

        guardar_rotinas(carregar_rotinas())


# ---------------- CASA ---------------- #

def carregar_casa():

    with open(FICHEIRO_CASA, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------- OBJETOS ---------------- #

def carregar_objetos():

    with open(FICHEIRO_OBJETOS, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------- RONDA ---------------- #

def ronda():

    casa = carregar_casa()

    objetos = carregar_objetos()

    encontrados = 0

    print("\n==============================")
    print("🤖 A iniciar ronda...")
    print("==============================\n")

    for divisao in casa["divisoes"]:

        print(f"\n📍 {divisao}")

        existe = False

        for nome, dados in objetos.items():

            if dados["divisao"] == divisao:

                existe = True

                print(
                    f"   ✔ {nome}"
                )

                encontrados += 1

        if not existe:

            print("   (Nenhum objeto registado)")

    print("\n==============================")
    print("Ronda concluída.")
    print(f"Objetos verificados: {encontrados}")
    print("==============================")

    print("\n🤖 A regressar à base...")

    print(
        f"Base: {casa['base']}"
    )


# ---------------- VER ROTINAS ---------------- #

def ver_rotinas():

    dados = carregar_rotinas()

    print("\n====== ROTINAS ======\n")

    for i, rotina in enumerate(dados["rotinas"], start=1):

        print(
            f"{i}. {rotina['nome']} ({rotina['hora']})"
        )

    print()


# ---------------- VERIFICAR ---------------- #

def verificar_rotinas():

    agora = datetime.now().strftime("%H:%M")

    dados = carregar_rotinas()

    for rotina in dados["rotinas"]:

        if rotina["hora"] == agora:

            print(f"\n⏰ {rotina['nome']}")

            if rotina["acao"] == "ronda":

                ronda()


if __name__ == "__main__":

    criar_ficheiro()

    ver_rotinas()

    ronda()