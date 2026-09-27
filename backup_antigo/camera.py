import cv2

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    if not ret:
        print("Não consegui abrir a webcam.")
        break

    cv2.imshow("Webcam do Accio", frame)

    tecla = cv2.waitKey(1)

    if tecla == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()