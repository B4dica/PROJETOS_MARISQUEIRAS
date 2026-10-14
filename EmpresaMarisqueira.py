class EmpresaMarisqueira:
    def __init__(self, id_empresa_marisqueira="", nome="", localizacao=""):
        self.id_empresa_marisqueira = id_empresa_marisqueira  # CNPJ
        self.nome = nome
        self.localizacao = localizacao

if __name__ == "__main__":
    # exemplo de uso
    emp = EmpresaMarisqueira(id_empresa_marisqueira="12.345.678/0001-99",
                             nome="Marisqueira Exemplo",
                             localizacao="Ilha Exemplo")
    print("EmpresaMarisqueira:")
    print(f"  ID (CNPJ): {emp.id_empresa_marisqueira}")
    print(f"  Nome: {emp.nome}")
    print(f"  Localização: {emp.localizacao}")