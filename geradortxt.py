import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class Geradortxt:

    def __init__(self, nome: str, corpo: str):
        self.nome = nome
        self.corpo = corpo

    def criar_txt(self):
        arquivo = open(f"{DIR_PATH}/{self.nome}.txt", "w")
        arquivo.write(self.corpo)
        arquivo.close()

