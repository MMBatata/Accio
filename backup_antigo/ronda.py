from visao import observar
from navegacao import ir_para

DIVISOES = [
    "Hall de entrada",
    "Sala",
    "Cozinha",
    "Corredor",
    "Quarto 1",
    "Quarto 2",
    "WC 1",
    "WC 2"
]

def ronda_casa():

    print("\n🤖 A iniciar ronda da casa...\n")

    memoria = {}

    for divisao in DIVISOES:

        print(f"\n========== {divisao} ==========\n")

        ir_para(divisao)


        objetos = observar(divisao)

        memoria[divisao] = objetos

    print("\n✅ Ronda concluída!")

    return memoria


if __name__ == "__main__":

    ronda_casa()