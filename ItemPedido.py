class ItemPedido:
    def __init__(self):
        self.produto = None  # Produto
        self.quantidade = 0  # em kg

    def adicionar_item(self, produto, quantidade):
        """Define produto e quantidade do item."""
        self.produto = produto
        self.quantidade = quantidade
        return self

    def validar_quantidade(self):
        """Delegando validação ao produto."""
        if self.produto is None:
            return False, "Produto não definido."
        return self.produto.validar_quantidade(self.quantidade)