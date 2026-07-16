from mapa import locais
from robot import executar_missao


def criar_missao(comando):

    comando = comando.lower()

    if "traz" in comando:
        acao = "trazer"

    elif "buscar" in comando or "busca" in comando:
        acao = "buscar"

    elif "procura" in comando:
        acao = "procurar"

    else:
        print("Não consegui perceber a missão.")
        return

    palavras_ignorar = {
        "accio",
        "traz",
        "traz-me",
        "buscar",
        "busca",
        "procura",
        "vai",
        "me",
        "o",
        "a",
        "os",
        "as",
        "um",
        "uma",
        "uns",
        "umas"
    }

    palavras = comando.split()

    objeto = []

    for palavra in palavras:
        if palavra not in palavras_ignorar:
            objeto.append(palavra)

    objeto = " ".join(objeto)

    objeto = (
    objeto.replace("ó", "o")
          .replace("á", "a")
          .replace("à", "a")
          .replace("â", "a")
          .replace("ã", "a")
          .replace("é", "e")
          .replace("ê", "e")
          .replace("í", "i")
          .replace("ú", "u")
          .replace("ç", "c")
)

    print("\n========== MISSÃO ==========")
    print("Ação:", acao)
    print("Objeto:", objeto)
    print("============================")

    guardar_missao(acao, objeto)

    print("Missão registada!")


def guardar_missao(acao, objeto):

    with open("missoes.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(f"{acao}|{objeto}|Pendente\n")


def ver_missoes():

    try:

        with open("missoes.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

        print("\n====== MISSÕES ======")

        numero = 1

        for linha in linhas:

            linha = linha.strip()

            if linha == "":
                continue

            dados = linha.split("|")

            if len(dados) != 3:
                continue

            acao, objeto, estado = dados

            print(f"{numero}. {acao} {objeto} - {estado}")

            numero += 1

        if numero == 1:
            print("Ainda não existem missões.")

        print("=====================")

    except FileNotFoundError:
        print("Ainda não existem missões.")


def iniciar_missao(numero):

    try:

        with open("missoes.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

        if numero < 1 or numero > len(linhas):
            print("Missão inexistente.")
            return

        dados = linhas[numero - 1].strip().split("|")

        dados[2] = "Em execução"

        linhas[numero - 1] = "|".join(dados) + "\n"

        with open("missoes.txt", "w", encoding="utf-8") as ficheiro:
            ficheiro.writelines(linhas)

        objeto = dados[1]

        local = locais.get(objeto, "local desconhecido")

        executar_missao(objeto, local)

        concluir_missao(numero)

    except FileNotFoundError:

        print("Não existe nenhum ficheiro de missões.")


def concluir_missao(numero):

    try:

        with open("missoes.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

        if numero < 1 or numero > len(linhas):
            print("Missão inexistente.")
            return

        dados = linhas[numero - 1].strip().split("|")

        acao = dados[0]
        objeto = dados[1]

        # Guardar no histórico
        guardar_historico(acao, objeto)
        atualizar_estatisticas(objeto)

        # Remover a missão concluída
        del linhas[numero - 1]

        with open("missoes.txt", "w", encoding="utf-8") as ficheiro:
            ficheiro.writelines(linhas)

        print("✅ Missão concluída e removida da lista!")

    except FileNotFoundError:
        print("Não existe nenhum ficheiro de missões.")

def trabalhar():

    try:

        with open("missoes.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

        encontrou = False

        for numero, linha in enumerate(linhas, start=1):

            dados = linha.strip().split("|")

            if len(dados) != 3:
                continue

            if dados[2] == "Pendente":

                encontrou = True

                print(f"\n🤖 A iniciar missão {numero}...")
                iniciar_missao(numero)

        if not encontrou:
            print("✅ Não existem missões pendentes.")

    except FileNotFoundError:
        print("Ainda não existem missões.")

def guardar_historico(acao, objeto):

    try:

        with open("historico.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

    except FileNotFoundError:

        linhas = []

    linhas.append(f"{acao}|{objeto}\n")

    if len(linhas) > 15:
        linhas = linhas[-15:]

    with open("historico.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.writelines(linhas)

def ver_historico():

    try:

        with open("historico.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

        print("\n====== HISTÓRICO ======")

        if len(linhas) == 0:
            print("Ainda não existem missões concluídas.")

        else:

            for i, linha in enumerate(linhas, start=1):

                dados = linha.strip().split("|")

                if len(dados) >= 2:

                    acao = dados[0]
                    objeto = dados[1]

                    print(f"{i}. {acao} {objeto}")

        print("=======================")

    except FileNotFoundError:

        print("Ainda não existe histórico.")
def atualizar_estatisticas(objeto):

    try:

        with open("estatisticas.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

    except FileNotFoundError:

        linhas = []

    estatisticas = {}

    for linha in linhas:

        dados = linha.strip().split("|")

        if len(dados) == 2:

            estatisticas[dados[0]] = int(dados[1])

    if objeto in estatisticas:

        estatisticas[objeto] += 1

    else:

        estatisticas[objeto] = 1

    with open("estatisticas.txt", "w", encoding="utf-8") as ficheiro:

        for obj, total in estatisticas.items():

            ficheiro.write(f"{obj}|{total}\n")

def ver_estatisticas():

    try:

        with open("estatisticas.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

        if len(linhas) == 0:
            print("Ainda não existem estatísticas.")
            return

        estatisticas = []

        for linha in linhas:

            objeto, total = linha.strip().split("|")

            estatisticas.append((objeto, int(total)))

        estatisticas.sort(key=lambda x: x[1], reverse=True)

        print("\n====== ESTATÍSTICAS ======")

        total_missoes = 0

        for objeto, vezes in estatisticas:

            print(f"📦 {objeto}: {vezes} vezes")
            total_missoes += vezes

        print("--------------------------")
        print(f"📊 Total de missões: {total_missoes}")
        print(f"🥇 Objeto mais procurado: {estatisticas[0][0]}")

        print("==========================")

    except FileNotFoundError:

        print("Ainda não existem estatísticas.")