from Empresa import Empresa

class EmpresaMarisqueira(Empresa):
    def __init__(self, nome="", localizacao, cnpj=""):
        super().__init__(nome, cnpj)
        # Pode ter atributos específicos se necessário
        self.tipo = "Marisqueira"
#vai herdar nome e localização, deixa apenas o cnpj
# produto se relaciona aqui
# o pedido se relaciona com ambos
#