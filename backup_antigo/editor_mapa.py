import tkinter as tk
from tkinter import simpledialog
import json

FICHEIRO = "planta.json"

janela = tk.Tk()
janela.title("Editor do Mapa - Accio")

inicio_x = 0
inicio_y = 0

retangulo = None
divisoes = []
portas = []
selecionada = None


def clicar(event):
    global inicio_x, inicio_y, retangulo

    inicio_x = event.x
    inicio_y = event.y

    retangulo = canvas.create_rectangle(
        inicio_x,
        inicio_y,
        inicio_x,
        inicio_y,
        outline="blue",
        width=2
    )


def arrastar(event):
    canvas.coords(
        retangulo,
        inicio_x,
        inicio_y,
        event.x,
        event.y
    )


def largar(event):

    nome = simpledialog.askstring(
        "Nova divisão",
        "Nome da divisão:"
    )

    if nome:

        canvas.create_text(
            (inicio_x + event.x) / 2,
            (inicio_y + event.y) / 2,
            text=nome,
            font=("Arial", 12, "bold")
        )

        divisoes.append({
            "nome": nome,
            "x1": inicio_x,
            "y1": inicio_y,
            "x2": event.x,
            "y2": event.y
        })

        print(divisoes)


def carregar_mapa():

    global divisoes

    try:

        with open(FICHEIRO, "r", encoding="utf-8") as f:
            divisoes = json.load(f)

        print("📂 Mapa carregado!")

    except FileNotFoundError:
        print("📂 Ainda não existe mapa.")
        return

    for divisao in divisoes:

        canvas.create_rectangle(
            divisao["x1"],
            divisao["y1"],
            divisao["x2"],
            divisao["y2"],
            outline="blue",
            width=2
        )

        canvas.create_text(
            (divisao["x1"] + divisao["x2"]) / 2,
            (divisao["y1"] + divisao["y2"]) / 2,
            text=divisao["nome"],
            font=("Arial", 12, "bold")
        )


def selecionar(event):

    global selecionada

    canvas.delete("selecionado")

    for divisao in divisoes:

        if (
            divisao["x1"] <= event.x <= divisao["x2"]
            and
            divisao["y1"] <= event.y <= divisao["y2"]
        ):

            selecionada = divisao["nome"]

            canvas.create_rectangle(
                divisao["x1"],
                divisao["y1"],
                divisao["x2"],
                divisao["y2"],
                outline="green",
                width=4,
                tags="selecionado"
            )

            print(f"✅ Divisão selecionada: {selecionada}")

            break

def guardar_portas():

    with open("portas.json", "w", encoding="utf-8") as f:

        json.dump(portas, f, indent=4, ensure_ascii=False)

    print("🚪 Portas guardadas!")

def adicionar_porta():

    origem = simpledialog.askstring(
        "Nova porta",
        "Divisão de origem:"
    )

    if origem is None:
        return

    destino = simpledialog.askstring(
        "Nova porta",
        "Divisão de destino:"
    )

    if destino is None:
        return

    portas.append({
        "origem": origem,
        "destino": destino
    })

    guardar_portas()

    print(f"🚪 Porta criada: {origem} ↔ {destino}")

def guardar_mapa():

    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(divisoes, f, indent=4, ensure_ascii=False)

    print("💾 Mapa guardado!")


# ---------- Interface ----------

barra = tk.Frame(janela)
barra.pack(fill="x")

botao_porta = tk.Button(
    barra,
    text="🚪 Nova porta",
    command=adicionar_porta
)

botao_porta.pack(side="left", padx=10)

botao = tk.Button(
    barra,
    text="💾 Guardar mapa",
    command=guardar_mapa
)

botao.pack(side="left", padx=10, pady=5)

canvas = tk.Canvas(
    janela,
    width=1000,
    height=700,
    bg="white"
)

canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", clicar)
canvas.bind("<B1-Motion>", arrastar)
canvas.bind("<ButtonRelease-1>", largar)
canvas.bind("<Button-3>", selecionar)

carregar_mapa()

janela.mainloop()