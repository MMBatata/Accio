def contem(comando, palavras):

    comando = comando.lower()

    for palavra in palavras:

        if palavra in comando:
            return True

    return False