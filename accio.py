from ultralytics import YOLO
import cv2
import time

from memoria_visual import atualizar

# Carrega o modelo apenas uma vez
modelo = YOLO("yolov8n.pt")

# Tradução dos nomes do YOLO
TRADUCAO = {
    "tv": "Televisão",
    "remote": "Comando da TV",
    "laptop": "Portátil",
    "bottle": "Garrafa de água",
    "chair": "Cadeira",
    "person": "Pessoa",
    "cell phone": "Telemóvel",
    "mouse": "Rato",
    "keyboard": "Teclado",
    "book": "Livro",
    "cup": "Copo"
}


def observar(divisao):

    print(f"\n📷 A observar a divisão: {divisao}\n")

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("❌ Não consegui abrir a webcam.")
        return []

    objetos = []

    inicio = time.time()

    while time.time() - inicio < 5:

        sucesso, frame = cam.read()

        if not sucesso:
            continue

        resultados = modelo(frame, verbose=False)

        for caixa in resultados[0].boxes:

            classe = int(caixa.cls[0])

            nome = modelo.names[classe]

            nome = TRADUCAO.get(nome, nome)

            if nome not in objetos:

                objetos.append(nome)

                print("👀", nome)

        frame = resultados[0].plot()

        cv2.imshow("Accio - Visão IA", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

    print("\n💾 A atualizar memória visual...\n")

    for objeto in objetos:
        atualizar(objeto, divisao)

    print("✅ Memória atualizada!")

    return objetos


if __name__ == "__main__":

    observar("Sala")