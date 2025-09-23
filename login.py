import tkinter as tk
from tkinter import messagebox
from instituicao import tela_principal_instituicao
from utils import menu_sair

def tela_login_instituicao(tela_inicial):
    login = tk.Tk()
    login.title("Login Instituição")
    login.geometry("300x250")

    tk.Label(login, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(login)
    entry_usuario.pack()

    tk.Label(login, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(login, show="*")
    entry_senha.pack()

    def verificar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario == "admin" and senha == "123":
            login.destroy()
            tela_principal_instituicao(tela_inicial)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    tk.Button(login, text="Entrar", command=verificar_login, bg="#2196F3", fg="white", width=8).pack(pady=20)
    tk.Button(login, text="Sair", width=8, command=lambda: menu_sair(login, tela_inicial), bg="#4CAF50", fg="white").pack(pady=10)

    login.mainloop()
