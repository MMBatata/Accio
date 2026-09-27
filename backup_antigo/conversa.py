from robot import accio_buscar_objeto

def executar_comando(comando):
    # Converte tudo para minúsculas e remove espaços a mais no início/fim
    comando = comando.lower().strip()

    # Verifica se a frase começa estritamente com a palavra mágica
    if comando.startswith("accio"):
        # Extrai o nome do objeto retirando a palavra "accio" da frente
        # Exemplo: "accio telemovel" vira "telemovel"
        objeto = comando.replace("accio", "", 1).strip()
        
        # Se o utilizador escreveu apenas "accio", sem o objeto
        if objeto == "":
            print("🤖 O feitiço falhou... Precisas de dizer o nome do objeto! Ex: 'Accio telemovel'")
        else:
            # Envia o objeto diretamente para os motores e sensores do robot.py
            accio_buscar_objeto(objeto)

    # Mantemos o estado apenas para veres se o robô está operacional
    elif comando == "estado" or comando == "bateria":
        print("🤖 Accio está operacional. A aguardar o teu feitiço!")

    elif comando == "ajuda":
        print("\n========== MANUAl DE FEITIÇOS ==========")
        print("• accio telemovel")
        print("• accio comando")
        print("• estado")
        print("========================================")

    else:
        print("❌ Nada aconteceu... Lembra-te de que eu só respondo ao feitiço 'Accio [objeto]'.")