from conversa import conversar
from calculadora import calculadora
from estado import estado_accio, relatorio
from memoria import dizer_local, saber_objeto
from tarefas import lista_tarefas

from missoes import (
    criar_missao,
    ver_missoes,
    concluir_missao,
    iniciar_missao,
    trabalhar,
    ver_historico,
    ver_estatisticas
)

from estado import estado_accio
from memoria import dizer_local


def executar_comando(comando):

    comando = comando.lower()

    # Conversar
    if (
        "conversar" in comando
        or "olá" in comando
        or "ola" in comando
    ):
        print("Accio: Vamos conversar!")
        conversar()

    # Calculadora
    elif (
        "calculadora" in comando
        or "contas" in comando
        or "calcular" in comando
    ):
        print("Accio: A abrir a calculadora...")
        calculadora()

    # Ver missões
    elif "missões" in comando or "missoes" in comando:
        ver_missoes()

    # Trabalhar automaticamente
    elif "trabalha" in comando:
        trabalhar()

    # Iniciar missão
    elif "iniciar" in comando:

        partes = comando.split()

        try:
            numero = int(partes[-1])
            iniciar_missao(numero)

        except ValueError:
            print("Escreve o número da missão.")

    # Concluir missão
    elif "concluir" in comando:

        partes = comando.split()

        try:
            numero = int(partes[-1])
            concluir_missao(numero)

        except ValueError:
            print("Escreve o número da missão.")

    # Criar missão
    elif (
        "traz" in comando
        or "buscar" in comando
        or "busca" in comando
        or "procura" in comando
    ):
        criar_missao(comando)

    # Lista de tarefas
    elif "tarefas" in comando:
        print("Accio: A abrir a lista de tarefas...")
        lista_tarefas()

    # Estado do Accio
    elif (
        "estado" in comando
        or "como estás" in comando
        or "como estas" in comando
    ):
        estado_accio()

    # Histórico
    elif (
        "historico" in comando
        or "histórico" in comando
    ):
        ver_historico()

    # Estatísticas
    elif (
        "estatisticas" in comando
        or "estatísticas" in comando
    ):
        ver_estatisticas()

    # Onde está um objeto?
    elif (
        "onde esta" in comando
        or "onde está" in comando
    ):

        palavras_ignorar = {
            "onde",
            "esta",
            "está",
            "o",
            "a",
            "os",
            "as"
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

        dizer_local(objeto)

    # Ajuda
    elif "ajuda" in comando:

        print("\n========== AJUDA ==========")
        print("• olá")
        print("• conversar")
        print("• calculadora")
        print("• tarefas")
        print("• missões")
        print("• iniciar missão 1")
        print("• trabalha")
        print("• estado")
        print("• histórico")
        print("• estatísticas")
        print("• onde estão os óculos")
        print("• traz os óculos")
        print("===========================")

    elif "o que sabes sobre" in comando:

        objeto = comando.replace("o que sabes sobre", "").strip()

        objeto = (
        objeto.replace("os ", "")
              .replace("as ", "")
              .replace("o ", "")
              .replace("a ", "")
              .replace("ó", "o")
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

        saber_objeto(objeto)

    elif "relatorio" in comando or "relatório" in comando:

        relatorio()

    else:
        print("Accio: Ainda não percebo esse comando.")