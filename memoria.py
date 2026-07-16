def carregar_memoria():

    memoria = {}

    try:

        with open("memoria.txt", "r", encoding="utf-8") as ficheiro:

            for linha in ficheiro:

                dados = linha.strip().split("|")

                if len(dados) == 2:
                    objeto = dados[0]
                    local = dados[1]

                    memoria[objeto] = local

    except FileNotFoundError:
        pass

    return memoria


def guardar_memoria(memoria):

    with open("memoria.txt", "w", encoding="utf-8") as ficheiro:

        for objeto, local in memoria.items():

            ficheiro.write(f"{objeto}|{local}\n")


def atualizar_memoria(objeto, local):

    memoria = carregar_memoria()

    memoria[objeto] = local

    guardar_memoria(memoria)

    def obter_local(objeto):

        memoria = carregar_memoria()

    if objeto in memoria:
        return memoria[objeto]

    return None

def obter_local(objeto):

    memoria = carregar_memoria()

    if objeto in memoria:
        return memoria[objeto]

    return None

def dizer_local(objeto):

    local = obter_local(objeto)

    if local is None:

        print(f"🧠 Ainda não sei onde está {objeto}.")

    else:

        print(f"🧠 Da última vez encontrei {objeto} em {local}.")

def saber_objeto(objeto):

    local = obter_local(objeto)

    try:

        with open("estatisticas.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

    except FileNotFoundError:

        linhas = []

    vezes = 0

    for linha in linhas:

        dados = linha.strip().split("|")

        if len(dados) == 2 and dados[0] == objeto:

            vezes = int(dados[1])

    print(f"\n🧠 Informações sobre {objeto}")

    if local is None:
        print("📍 Local: desconhecido")
    else:
        print(f"📍 Último local: {local}")

    print(f"📊 Procurado: {vezes} vezes")