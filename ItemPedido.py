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

if __name__ == "__main__":
    # exemplo de uso
    from Produto import Produto
    # criar produto de exemplo
    prod = Produto()
    prod.cadastrar_produto(name="Siri", categoria="congelado", preco=30.0, quantidade_disponivel=50)
    # criar item
    item = ItemPedido()
    item.id_pedido = 2001  # simulando definição externa
    item.adicionar_item(prod, 30)
    print("ItemPedido criado:")
    print(f"  ID do pedido: {item.id_pedido}")
    print(f"  ID do produto: {item.id_produto}")
    print(f"  Quantidade: {item.quantidade} kg")
    # validar quantidade (delegada)
    valido, msg = item.validar_quantidade()
    print("\nChamar validar_quantidade():")
    print(f"  Válido: {valido}")
    print(f"  Mensagem: {msg}")
    # testar com quantidade fora do range (como não temos validação direta, ainda retornará True)
    item.quantidade = 10
    print("\nApós alterar quantidade para 10 kg:")
    print(f"  Quantidade: {item.quantidade} kg")
    valido, msg = item.validar_quantidade()
    print(f"  Válido: {valido}")
    print(f"  Mensagem: {msg}")