class Produto:
    def __init__(self, nome="", categoria="", preco=0.0, quantidade=0, empresa=None):
        """
        categoria: 'fresco' ou 'congelado'
        quantidade: em kg
        empresa: EmpresaMarisqueira que vende o produto
        """
        self.nome = nome
        self.categoria = categoria.lower()  # fresco ou congelado
        self.preco = preco  # preço por kg
        self.quantidade = quantidade  # estoque disponível em kg
        self.empresa = empresa  # referência à empresa vendedora
        self.foto = None  # opcional, não obrigatório conforme RN

    def cadastrar_produto(self, nome, categoria, preco, quantidade, empresa):
        """Define os atributos do produto."""
        self.nome = nome
        self.categoria = categoria.lower()
        self.preco = preco
        self.quantidade = quantidade
        self.empresa = empresa
        return self

    def alterar_quantidade(self, nova_quantidade):
        """Altera a quantidade disponível (em kg)."""
        if nova_quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.quantidade = nova_quantidade

    def atualizar_quantidade(self, quantidade_adicional):
        """Adiciona ou subtrai quantidade no estoque."""
        nova_qtd = self.quantidade + quantidade_adicional
        if nova_qtd < 0:
            raise ValueError("Estoque não pode ficar negativo.")
        self.quantidade = nova_qtd

    def validar_quantidade(self, quantidade_solicitada):
        """Verifica se a quantidade solicitada é válida (mínimo 25 kg e disponível)."""
        if quantidade_solicitada < 25:
            return False, "Quantidade mínima de 25 kg não atingida."
        if quantidade_solicitada > self.quantidade:
            return False, "Estoque insuficiente."
        return True, "Quantidade válida."