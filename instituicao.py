import tkinter as tk
from tkinter import messagebox, ttk
import csv
from utils import carregar_cuidadores, carregar_convocacoes, menu_sair

def tela_principal_instituicao(tela_inicial):
    janela = tk.Tk()
    janela.title("Perfil Administrador")
    janela.geometry("400x250")

    tk.Label(janela, text="Perfil Administrador", font=("Arial", 14, "bold")).pack(pady=20)

    def lista_cuidadores():
        lista = tk.Toplevel(janela)
        lista.title("Cuidadores Cadastrados")
        lista.geometry("450x300")

        cols = ("Nome", "Telefone", "Formação")
        tree = ttk.Treeview(lista, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=140)
        tree.pack(fill="both", expand=True)

        for cuidador in carregar_cuidadores():
            tree.insert("", "end", values=(cuidador["Nome"], cuidador["Telefone"], cuidador["Formação"]))

    def lista_convocacao():
        lista = tk.Toplevel(janela)
        lista.title("Histórico de convocação")
        lista.geometry("450x300")

        cols = ("Data", "Periodo")
        tree = ttk.Treeview(lista, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=140)
        tree.pack(fill="both", expand=True)

        for convocacao in carregar_convocacoes():
            tree.insert("", "end", values=(convocacao["Data"], convocacao["Período"]))

    def convocar():
        def salvar_convocacao(data, periodo):
            with open("convocacoes.csv", mode="a", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                if f.tell() == 0:
                    escritor.writerow(["Data", "Período"])
                escritor.writerow([data, periodo])

        def enviar_convocacao():
            data = entry_data.get()
            periodo = entry_periodo.get()
            if data and periodo:
                salvar_convocacao(data, periodo)
                messagebox.showinfo("Convocação", f"Convocação enviada para o período: {periodo}")
                popup.destroy()
            else:
                messagebox.showwarning("Atenção", "Informe o período do plantão!")

        popup = tk.Toplevel(janela)
        popup.title("Dados do plantão:")
        popup.geometry("300x200")

        tk.Label(popup, text="Data do Plantão:").pack(pady=5)
        entry_data = tk.Entry(popup, width=30)
        entry_data.pack()
        tk.Label(popup, text="Período do Plantão:").pack(pady=5)
        entry_periodo = tk.Entry(popup, width=30)
        entry_periodo.pack()

        tk.Button(popup, text="Enviar Convocação", command=enviar_convocacao, bg="#4CAF50", fg="white").pack(pady=20)

    tk.Button(janela, text="Listar Cuidadores", width=25, command=lista_cuidadores).pack(pady=10)
    tk.Button(janela, text="Convocar para Plantão", width=25, command=convocar).pack(pady=10)
    tk.Button(janela, text="Histórico de convocação", width=25, command=lista_convocacao).pack(pady=10)
    tk.Button(janela, text="Sair", width=25, command=lambda: menu_sair(janela, tela_inicial),bg="#4CAF50", fg="white").pack(pady=10)

    janela.mainloop()
