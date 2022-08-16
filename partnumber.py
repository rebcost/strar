import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class PartNumber:

    def extrair_pn(self):
        partnumber = []
        arquivo = open(f"{DIR_PATH}/PN_CADASTRO.txt", "r")
        for pn in arquivo.readlines():
            index = pn.find(":")
            partnumber.append(pn[index + 1:].strip())
        return partnumber

    def pn_base(self):
        pn = self.extrair_pn()
        return pn[0]

    def pn_cadastrar(self):
        pn = self.extrair_pn()
        return pn[1]

