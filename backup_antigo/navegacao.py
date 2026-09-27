import json
import time

from visualizacao import mostrar_mapa
from estado import estado


FICHEIRO_PORTAS = "portas.json"


def carregar_portas():

    try:
        with open(FICHEIRO_PORTAS, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []


def construir_grafo():

    portas = carregar_portas()

    grafo = {}

    for porta in portas:

        origem = porta["origem"].lower()
        destino = porta["destino"].lower()

        if origem not in grafo:
            grafo[origem] = []

        if destino not in grafo:
            grafo[destino] = []

        grafo[origem].append(destino)
        grafo[destino].append(origem)

    return grafo


def encontrar_caminho(origem, destino):

    origem = origem.lower()
    destino = destino.lower()

    grafo = construir_grafo()

    visitados = []
    fila = [(origem, [origem])]

    while fila:

        atual, caminho = fila.pop(0)

        if atual == destino:
            return caminho

        if atual not in visitados:

            visitados.append(atual)

            for vizinho in grafo.get(atual, []):

                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    return None


def percorrer_caminho(caminho):

    if caminho is None:

        print("❌ Não existe caminho.")
        return

    print("\n🗺️ Percurso calculado:\n")

    for divisao in caminho:
        print("➡️", divisao.capitalize())

    print("\n🚶 A deslocar-me...\n")

    for divisao in caminho:

        estado["posicao"] = divisao

        try:
            mostrar_mapa(divisao)
        except:
            pass

        print("🤖 Estou em:", divisao.capitalize())

        time.sleep(2)

    print("\n✅ Destino alcançado!")


from estado import estado

def ir_para(destino):

    origem = estado["posicao"]

    caminho = encontrar_caminho(origem, destino)

    if caminho is None:
        print(f"❌ Não existe caminho até {destino}.")
        return False

    percorrer_caminho(caminho)

    return True