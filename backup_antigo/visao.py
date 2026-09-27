from ultralytics import YOLO
import cv2
from mapa_mental import atualizar as atualizar_mapa
from memoria_visual import atualizar
from cerebro import atualizar_objeto

modelo = YOLO("yolov8n.pt")

TRADUCAO = {
    "person": "Pessoa",
    "tv": "Televisão",
    "remote": "Comando da TV",
    "laptop": "Portátil",
    "cell phone": "Telemóvel",
    "chair": "Cadeira",
    "bottle": "Garrafa de água",
    "book": "Livro",
    "cup": "Copo",
    "keyboard": "Teclado",
    "mouse": "Rato"
}

OBJETOS_IMPORTANTES = {
    "Pessoa",
    "Televisão",
    "Comando da TV",
    "Portátil",
    "Telemóvel",
    "Cadeira",
    "Garrafa de água",
    "Livro",
    "Copo",
    "Teclado",
    "Rato"
}


def observar(divisao):

    print(f"\n📷 A observar a divisão: {divisao}\n")

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cam.isOpened():
        print("❌ Não consegui abrir a webcam.")
        return []

    objetos = []
    ultima_vez_visto = {}
    contador = {}

    while True:

        sucesso, frame = cam.read()

        if not sucesso:
            break

        resultados = modelo(frame, verbose=False)

        for caixa in resultados[0].boxes:

            classe = int(caixa.cls[0])

            confianca = float(caixa.conf[0])

            nome = modelo.names[classe]

            nome = TRADUCAO.get(nome, nome)

            if confianca < 0.60:
                continue

            if nome not in OBJETOS_IMPORTANTES:
                continue

            contador[nome] = contador.get(nome, 0) + 1
            ultima_vez_visto[nome] = cv2.getTickCount()

            if contador[nome] >= 10:

                if nome not in objetos:

                    objetos.append(nome)

                    print(f"👀 {nome} ({confianca*100:.1f}%)")

        imagem = resultados[0].plot()

        cv2.imshow("Accio - Visão IA", imagem)

        tecla = cv2.waitKey(1)

        if tecla == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

    print("\n💾 A guardar memória...\n")

    for objeto in objetos:

        atualizar(objeto, divisao)

        atualizar_objeto(objeto, divisao)

    atualizar_mapa(divisao, objetos)

    print("✅ Memória visual atualizada!")
    print("🧠 Mapa mental atualizado!")
    print("🧠 Cérebro atualizado!")

    return objetos


if __name__ == "__main__":

    observar("Sala")