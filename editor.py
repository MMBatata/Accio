import json
import os

FICHEIRO = "casa.json"


def carregar():
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "base": "",
        "divisoes": {}
    }


def guardar(casa):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(casa, f, indent=4, ensure_ascii=False)


def ver_divisoes(casa):

    print("\n===== DIVISÕES =====")

    if len(casa["divisoes"]) == 0:
        print("Ainda não existem divisões.")
        return

    for nome, dados in casa["divisoes"].items():

        print(f"\n📍 {nome}")

        print(" Liga a:")

        for l in dados["liga"]:
            print("  -", l)

        print(" Obstáculos:")

        if len(dados["obstaculos"]) == 0:
            print("  Nenhum")

        else:
            for o in dados["obstaculos"]:
                print("  -", o)


def criar_divisao(casa):

    nome = input("Nome da divisão: ").strip()

    if nome in casa["divisoes"]:
        print("Essa divisão já existe.")
        return

    casa["divisoes"][nome] = {
        "liga": [],
        "obstaculos": [],
        "objetos": []
    }

    print("Divisão criada.")


def ligar_divisoes(casa):

    a = input("Primeira divisão: ").strip()
    b = input("Segunda divisão: ").strip()

    if a not in casa["divisoes"]:
        print("Divisão inexistente.")
        return

    if b not in casa["divisoes"]:
        print("Divisão inexistente.")
        return

    if b not in casa["divisoes"][a]["liga"]:
        casa["divisoes"][a]["liga"].append(b)

    if a not in casa["divisoes"][b]["liga"]:
        casa["divisoes"][b]["liga"].append(a)

    print("Ligação criada.")


def adicionar_obstaculo(casa):

    divisao = input("Divisão: ").strip()

    if divisao not in casa["divisoes"]:
        print("Divisão inexistente.")
        return

    obstaculo = input("Nome do obstáculo: ").strip()

    casa["divisoes"][divisao]["obstaculos"].append(obstaculo)

    print("Obstáculo adicionado.")

def adicionar_objeto(casa):

    divisao = input("Divisão: ").strip()

    if divisao not in casa["divisoes"]:
        print("Divisão inexistente.")
        return

    objeto = input("Nome do objeto: ").strip()

    casa["divisoes"][divisao]["objetos"].append(objeto)

    print("Objeto registado.")

def definir_base(casa):

    divisao = input("Onde começa o Accio? ").strip()

    if divisao not in casa["divisoes"]:
        print("Divisão inexistente.")
        return

    casa["base"] = divisao

    print("Base definida.")


def menu():

    casa = carregar()

    while True:

        print("1 - Ver divisões")
        print("2 - Criar divisão")
        print("3 - Ligar divisões")
        print("4 - Adicionar obstáculo")
        print("5 - Adicionar objeto")
        print("6 - Definir base")
        print("7 - Guardar")
        print("8 - Sair")

        op = input("\nEscolha: ")

        if op == "1":
            ver_divisoes(casa)

        elif op == "2":
            criar_divisao(casa)

        elif op == "3":
            ligar_divisoes(casa)

        elif op == "4":
            adicionar_obstaculo(casa)

        elif op == "5":
            adicionar_objeto(casa)

        elif op == "6":
            definir_base(casa)

        elif op == "7":
            guardar(casa)

        elif op == "8":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()