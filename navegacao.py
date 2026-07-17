from casa import casa


def encontrar_caminho(origem, destino):

    visitados = []
    fila = [(origem, [origem])]

    while fila:

        atual, caminho = fila.pop(0)

        if atual == destino:
            return caminho

        if atual not in visitados:

            visitados.append(atual)

            for vizinho in casa[atual]["liga"]:

                fila.append((vizinho, caminho + [vizinho]))

    return None

import time


def percorrer_caminho(caminho):

    print("\n🗺️ Percurso calculado:\n")

    for divisao in caminho:
        print(f"➡️ {divisao.capitalize()}")
        time.sleep(2)

    print("\n🚶 A deslocar-me...\n")

    for divisao in caminho:
        print(f"📍 Estou em: {divisao.capitalize()}")
        time.sleep(2)

    print("\n✅ Destino alcançado!")