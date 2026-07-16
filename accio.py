from conversa import conversar
from calculadora import calculadora
from tarefas import lista_tarefas, carregar_tarefas
from comandos import executar_comando


def menu():
    print("\n==============================")
    print("        ACCIO V3")
    print("==============================")
    print("1 - Conversar")
    print("2 - Calculadora")
    print("3 - Lista de tarefas")
    print("4 - Modo Comandos")
    print("5 - Sair")


carregar_tarefas()

while True:

    menu()

    try:
        opcao = int(input("\nEscolhe uma opção: "))

    except ValueError:
        print("Escreve um número válido.")
        continue

    if opcao == 1:

        conversar()

    elif opcao == 2:

        calculadora()

    elif opcao == 3:

        lista_tarefas()

    elif opcao == 4:

        print("\n=== MODO COMANDOS ===")

        while True:

            comando = input("\nAccio> ")

            if comando.lower() == "voltar":
                break

            executar_comando(comando)

    elif opcao == 5:

        print("\nAté breve!")
        break

    else:

        print("Opção inválida.")