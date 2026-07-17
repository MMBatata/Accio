estado = {
    "local": "base",
    "posicao": "hall",
    "bateria": 100,
    "ocupado": False,
    "a_transportar": None
}


def estado_accio():

    print("\n===== ESTADO DO ACCIO =====")
    print(f"📍 Local: {estado['local']}")
    print(f"🔋 Bateria: {estado['bateria']}%")

    if estado["ocupado"]:
        print("💼 Estado: Ocupado")
    else:
        print("💼 Estado: Disponível")

    if estado["a_transportar"] is None:
        print("📦 A transportar: Nada")
    else:
        print(f"📦 A transportar: {estado['a_transportar']}")

    print("===========================")
def gastar_bateria(percentagem):

    estado["bateria"] -= percentagem

    if estado["bateria"] < 0:
        estado["bateria"] = 0


def carregar_bateria():

    print("\n🔌 A ligar ao carregador...")

    while estado["bateria"] < 100:

        estado["bateria"] += 10

        if estado["bateria"] > 100:
            estado["bateria"] = 100

        print(f"🔋 {estado['bateria']}%")

        import time
        time.sleep(0.5)

    print("✅ Bateria totalmente carregada!")

    import os

def relatorio():

    print("\n🤖 ===== RELATÓRIO =====")

    print(f"📍 Local: {estado['local']}")
    print(f"🔋 Bateria: {estado['bateria']}%")

    if estado["ocupado"]:
        print("⚙️ Estado: Ocupado")
    else:
        print("⚙️ Estado: Livre")

    if estado["a_transportar"] is None:
        print("📦 A transportar: Nada")
    else:
        print(f"📦 A transportar: {estado['a_transportar']}")

    try:
        with open("missoes.txt", "r", encoding="utf-8") as f:
            print(f"📋 Missões pendentes: {len(f.readlines())}")
    except:
        print("📋 Missões pendentes: 0")

    try:
        with open("historico.txt", "r", encoding="utf-8") as f:
            print(f"📜 Histórico: {len(f.readlines())} missões")
    except:
        print("📜 Histórico: 0")

    try:
        with open("memoria.txt", "r", encoding="utf-8") as f:
            print(f"🧠 Objetos conhecidos: {len(f.readlines())}")
    except:
        print("🧠 Objetos conhecidos: 0")

    print("=========================")