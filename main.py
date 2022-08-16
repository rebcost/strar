import os
from geradortxt import Geradortxt
from starweb import Starweb


if not os.path.isfile("PN_CADASTRO.txt"):
    g = Geradortxt("PN_CADASTRO", "PN_BASE: \nPN_CADASTRAR: ")
    g.criar_txt()
    # TODO: Criar uma janela de erro que mostra a mensagem abaixo
    print("Arquivo txt criado. Inserir as informações antes de continuar")
    exit()

Starweb()


