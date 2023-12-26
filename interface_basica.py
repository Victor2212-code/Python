import tkinter as tk
from tkinter import ttk


class MinhaGUI:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Minha GUI Profissional")
        self.janela.iconbitmap("./imagens/ico.png")

        largura_janela = 400
        altura_janela = 200
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        self.janela.geometry(
            f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        self.janela.configure(borderwidth=2, relief="groove")

        self.fundo = tk.PhotoImage(file="imagens/Amorim Coder (2).png")
        self.label_fundo = tk.Label(self.janela, image=self.fundo)
        self.label_fundo.place(relwidth=1, relheight=1)

        self.label = tk.Label(
            self.janela, text="Bem-vindo à Minha GUI Profissional", font=("Arial", 18))
        self.label.pack(pady=20)

        self.entrada_nome = tk.Entry(self.janela, font=("Arial", 12))
        self.entrada_nome.insert(0, "Seu Nome")
        self.entrada_nome.pack(pady=10)

        estilo = ttk.Style()
        estilo.configure("My.TButton", font=("Arial", 14),
                         background="#3366CC", foreground="white")
        self.botao = ttk.Button(self.janela, text="Clique em mim",
                                command=self.mostrar_mensagem, style="My.TButton")
        self.botao.pack()

    def mostrar_mensagem(self):
        nome = self.entrada_nome.get()
        if nome:
            self.label.config(text=f"Olá, {nome}!")


def main():
    janela = tk.Tk()
    app = MinhaGUI(janela)
    janela.mainloop()


if __name__ == "__main__":
    main()
