import tkinter as tk
from cadastro import tela_cadastro_cuidador
from login import tela_login_instituicao

def tela_inicial():
    janela = tk.Tk()
    janela.title("Sistema de Gestão de Cuidadores")
    janela.geometry("400x250")

    tk.Label(janela, text="Bem-vindo!", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(janela, text="Selecione seu perfil para continuar:").pack(pady=10)

    def abrir_cadastro():
        janela.destroy()
        tela_cadastro_cuidador(tela_inicial)

    def abrir_login():
        janela.destroy()
        tela_login_instituicao(tela_inicial)

    tk.Button(janela, text="Sou Cuidador - Cadastrar", width=25, command=abrir_cadastro).pack(pady=10)
    tk.Button(janela, text="Administrador", width=25, command=abrir_login).pack(pady=10)

    janela.mainloop()
