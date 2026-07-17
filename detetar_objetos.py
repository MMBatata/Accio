from ultralytics import YOLO
import cv2

# Carrega o modelo apenas uma vez
modelo = YOLO("yolov8n.pt")


def observar(divisao="Desconhecida"):

    print(f"\n📷 A observar: {divisao}")

    cam = cv2.VideoCapture(0)

    sucesso, frame = cam.read()

    if not sucesso:
        print("Erro ao abrir a webcam.")
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

    return objetos


if __name__ == "__main__":

    observar("Teste")