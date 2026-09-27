import tkinter as tk
import json

from estado import estado

FICHEIRO = "planta.json"

janela = tk.Tk()
janela.title("Mapa Mental do Accio")

canvas = tk.Canvas(janela, width=1300, height=500, bg="white")
canvas.pack()

robo = None


def carregar_planta():

    with open(FICHEIRO, "r", encoding="utf-8") as f:
        return json.load(f)


def desenhar():

    global robo

    canvas.delete("all")

    planta = carregar_planta()

    for item in planta:

        nome = item["nome"]

        x1 = item["x1"]
        y1 = item["y1"]
        x2 = item["x2"]
        y2 = item["y2"]

        if nome == "porta":

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill="brown",
                outline="brown"
            )

            continue

        canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            outline="blue",
            width=2
        )

        canvas.create_text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            text=nome,
            font=("Arial", 12, "bold")
        )

        if nome.lower() == estado["posicao"].lower():

            robo = canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2 + 25,
                text="🤖",
                font=("Arial", 20)
            )

    janela.after(200, desenhar)


def iniciar():

    desenhar()

    janela.mainloop()