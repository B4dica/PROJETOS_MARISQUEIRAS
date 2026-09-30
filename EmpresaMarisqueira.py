from Empresa import Empresa

class EmpresaMarisqueira(Empresa):
    def __init__(self, nome="", cnpj=""):
        super().__init__(nome, cnpj)
        # Pode ter atributos específicos se necessário
        self.tipo = "Marisqueira"