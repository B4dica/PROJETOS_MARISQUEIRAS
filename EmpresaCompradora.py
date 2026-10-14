class EmpresaCompradora:
    def __init__(self, id_empresa_compradora="", nome="", localizacao=""):
        self.id_empresa_compradora = id_empresa_compradora  # CNPJ
        self.nome = nome
        self.localizacao = localizacao

if __name__ == "__main__":
    # exemplo de uso
    emp = EmpresaCompradora(id_empresa_compradora="98.765.432/0001-11",
                            nome="Compradora Exemplo",
                            localizacao="Centro Exemplo")
    print("EmpresaCompradora:")
    print(f"  ID (CNPJ): {emp.id_empresa_compradora}")
    print(f"  Nome: {emp.nome}")
    print(f"  Localização: {emp.localizacao}")