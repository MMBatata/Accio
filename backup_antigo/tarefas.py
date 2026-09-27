tarefas = []


def carregar_tarefas():
    global tarefas

    try:
        with open("tarefas.txt", "r", encoding="utf-8") as ficheiro:
            tarefas = []

            for linha in ficheiro:
                linha = linha.strip()

                if linha != "":
                    tarefas.append(linha)

    except FileNotFoundError:
        tarefas = []


def guardar_tarefas():
    with open("tarefas.txt", "w", encoding="utf-8") as ficheiro:
        for tarefa in tarefas:
            ficheiro.write(tarefa + "\n")


def lista_tarefas():

    while True:

        print("\n~~~ Lista de tarefas ~~~")
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefas")
        print("3 - Apagar tarefa")
        print("4 - Voltar")

        try:
            opcao = int(input("Escolhe uma opção: "))
        except ValueError:
            print("Escreve um número válido!")
            continue

        if opcao == 1:
            tarefa = input("Escreve a tarefa: ")

            tarefas.append(tarefa)
            guardar_tarefas()

            print("Tarefa adicionada!")

        elif opcao == 2:

            if len(tarefas) == 0:
                print("Não existem tarefas.")
            else:
                print("\n--- As tuas tarefas ---")
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1} - {tarefa}")

        elif opcao == 3:

            if len(tarefas) == 0:
                print("Não existem tarefas para apagar.")
            else:
                print("\n--- As tuas tarefas ---")
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1} - {tarefa}")

                try:
                    numero = int(input("Qual tarefa queres apagar? "))

                    if 1 <= numero <= len(tarefas):
                        apagada = tarefas.pop(numero - 1)
                        guardar_tarefas()
                        print(f"Tarefa '{apagada}' apagada!")
                    else:
                        print("Número inválido!")

                except ValueError:
                    print("Escreve um número válido!")

        elif opcao == 4:
            break

        else:
            print("Opção inválida!")