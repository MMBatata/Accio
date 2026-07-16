import time
from memoria import obter_local, atualizar_memoria
from estado import estado, gastar_bateria, carregar_bateria


def executar_missao(objeto, local):

    if estado["bateria"] < 20:

        print("⚠️ Bateria fraca.")

    carregar_bateria()

    print("\n🤖 Missão iniciada!")
    time.sleep(1)
    estado["ocupado"] = True
    estado["a_transportar"] = objeto

    # 1 - Verificar a memória
    ultimo_local = obter_local(objeto)

    if ultimo_local is not None:

        print(f"🧠 Lembro-me de ter visto {objeto} em {ultimo_local}.")
        time.sleep(1)

        print(f"🚶 Vou primeiro a {ultimo_local}...")
        time.sleep(2)

        print("🚪 A entrar na divisão...")
        time.sleep(1)
        gastar_bateria(10)

        print("👀 A observar o ambiente...")
        time.sleep(2)
        gastar_bateria(5)

        print("🔎 A verificar as superfícies...")
        time.sleep(2)

        print(f"🔍 À procura de {objeto}...")
        time.sleep(2)

        resposta = input(
            f"\n👤 O {objeto} estava em {ultimo_local}? (s/n): "
        ).lower()

        if resposta == "s":

            print(f"📦 Encontrei {objeto}!")
            time.sleep(2)

            print("↩️ A regressar...")
            time.sleep(2)
            gastar_bateria(10)

            print("🎁 Objeto entregue!")
            estado["ocupado"] = False
        estado["a_transportar"] = None
        estado["local"] = "base"
        return

        print("🤔 Já não estava lá...")
        time.sleep(2)

    # 2 - Ir ao local do mapa
    if local != "local desconhecido":

        
        estado["local"] = local
        print(f"\n📍 Vou ao local conhecido: {local}")
        time.sleep(2)

        print("🚪 A entrar na divisão...")
        time.sleep(1)
        gastar_bateria(10)

        print("👀 A observar o ambiente...")
        time.sleep(2)
        gastar_bateria(5)

        print("🔎 A verificar as superfícies...")
        time.sleep(2)

        print(f"🔍 À procura de {objeto}...")
        time.sleep(2)
        gastar_bateria(5)

        resposta = input(
            f"\n👤 O {objeto} estava em {local}? (s/n): "
        ).lower()

        if resposta == "s":

            print(f"📦 Encontrei {objeto}!")
            atualizar_memoria(objeto, local)

            time.sleep(2)

            print("↩️ A regressar...")
            time.sleep(2)
            gastar_bateria(10)

            print("🎁 Objeto entregue!")
            estado["ocupado"] = False
        estado["a_transportar"] = None
        estado["local"] = "base"
        return
        

        print("🤔 Também não estava lá.")
        time.sleep(2)

    # 3 - Procurar pela casa
    print("\n🏠 Vou procurar pela casa...")
    time.sleep(2)

    print("🚪 A percorrer a casa...")
    time.sleep(2)
    gastar_bateria(10)

    print("👀 A observar todas as divisões...")
    time.sleep(2)
    gastar_bateria(5)

    print(f"🔍 Ainda à procura de {objeto}...")
    time.sleep(2)

    novo_local = input(
        "\n👤 Em que divisão encontraste o objeto? "
    )

    estado["local"] = novo_local

    atualizar_memoria(objeto, novo_local)

    print("\n🧠 Memória atualizada!")
    print(f"Da próxima vez vou procurar primeiro em {novo_local}.")
    time.sleep(2)

    print("📦 Objeto encontrado!")
    time.sleep(2)

    print("↩️ A regressar...")
    time.sleep(2)
    gastar_bateria(10)

    print("🎁 Objeto entregue!")

    estado["ocupado"] = False
estado["a_transportar"] = None
estado["local"] = "base"