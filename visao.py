from ultralytics import YOLO
import cv2
from memoria_visual import atualizar

# Carrega o modelo apenas uma vez
modelo = YOLO("yolov8n.pt")


def observar(divisao):

    print(f"\n📷 A observar a divisão: {divisao}")

    cam = cv2.VideoCapture(0)

    sucesso, frame = cam.read()

    if not sucesso:
        print("❌ Não consegui abrir a webcam.")
        cam.release()
        return []

    resultados = modelo(frame, verbose=False)

    objetos = []

    for caixa in resultados[0].boxes:

        classe = int(caixa.cls[0])

        nome = modelo.names[classe]

        if nome not in objetos:
            objetos.append(nome)

    cam.release()

    print("\n👀 Objetos encontrados:")

    for objeto in objetos:
        print("✔", objeto)

    # Guarda na memória visual
    atualizar(objetos, divisao)

    return objetos


if __name__ == "__main__":

    observar("Sala")