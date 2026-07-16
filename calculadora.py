def calculadora():
    print("=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    escolha = int(input("Escolhe uma opção: "))

    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    if escolha == 1:
        print("Resultado:", n1 + n2)

    elif escolha == 2:
        print("Resultado:", n1 - n2)

    elif escolha == 3:
        print("Resultado:", n1 * n2)

    elif escolha == 4:
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Não podes dividir por zero!")

    else:
        print("Opção inválida!")