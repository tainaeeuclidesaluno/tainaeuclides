import tkinter as tk
from tkinter import messagebox
from utils import salvar_cuidador, menu_sair

def tela_cadastro_cuidador(tela_inicial):
    cadastro = tk.Tk()
    cadastro.title("Perfil do Candidato")
    cadastro.geometry("350x300")

    tk.Label(cadastro, text="Preencha seus dados:", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Label(cadastro, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(cadastro, width=30)
    entry_nome.pack()

    tk.Label(cadastro, text="Telefone:").pack(pady=5)
    entry_tel = tk.Entry(cadastro, width=30)
    entry_tel.pack()

    tk.Label(cadastro, text="Formação:").pack(pady=5)
    entry_form = tk.Entry(cadastro, width=30)
    entry_form.pack()

    def salvar():
        nome = entry_nome.get()
        tel = entry_tel.get()
        formacao = entry_form.get()
        if nome and tel and formacao:
            salvar_cuidador(nome, tel, formacao)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!\nAguarde convocação.")
            cadastro.destroy()
            tela_inicial()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")

    tk.Button(cadastro, text="Salvar Cadastro", command=salvar, bg="#2196F3", fg="white", width=20).pack(pady=20)
    tk.Button(cadastro, text="Sair", width=20, command=lambda: menu_sair(cadastro, tela_inicial), bg="#4CAF50", fg="white").pack(pady=5)

    cadastro.mainloop()
