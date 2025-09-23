import csv
import os

ARQUIVO1 = "cuidadores.csv"
ARQUIVO2 = "convocacoes.csv"

def salvar_cuidador(nome, telefone, formacao):
    existe = os.path.isfile(ARQUIVO1)
    with open(ARQUIVO1, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if not existe:
            escritor.writerow(["Nome", "Telefone", "Formação"])
        escritor.writerow([nome, telefone, formacao])

def carregar_cuidadores():
    cuidadores = []
    if os.path.isfile(ARQUIVO1):
        with open(ARQUIVO1, newline="", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for row in leitor:
                cuidadores.append(row)
    return cuidadores

def carregar_convocacoes():
    convocacoes = []
    if os.path.isfile(ARQUIVO2):
        with open(ARQUIVO2, newline="", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for row in leitor:
                convocacoes.append(row)
    return convocacoes

def menu_sair(janela, tela_inicial):
    janela.destroy()
    tela_inicial()
