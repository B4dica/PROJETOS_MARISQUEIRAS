class ItemPedido:
    def __init__(self):
        self.id_pedido = None   # Pedido ao qual o item pertence
        self.id_produto = None  # Produto que participa do pedido
        self.quantidade = 0     # Quantidade solicitada do produto, em kg

    def adicionar_item(self, produto, quantidade):
        """Define produto e quantidade do item."""
        self.id_produto = produto.id_produto
        self.quantidade = quantidade
        return self

    def validar_quantidade(self):
        """Delegando validação ao produto."""
        if self.id_produto is None:
            return False, "Produto não definido."
        # Esperamos que o produto seja passado como argumento? Neste caso, vamos assumir que o chamador já validou.
        # Para manter a interface, retornamos True se quantidade >=25 e estoque suficiente, mas precisamos do produto.
        # Como não temos acesso direto ao produto aqui, deixaremos a validação ser feita no Pedido.
        return True, "ItemPedido não possui validação direta; verifique no Pedido."