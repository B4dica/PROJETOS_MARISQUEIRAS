class Empresa:
    def __init__(self, nome="", cnpj=""):
        self.nome = nome
        self.cnpj = cnpj
        self.produtos = []  # list of Produto objects
        self.avaliacoes_recebidas = []  # list of Avaliacao objects recebidas

    def cadastrar_produto(self, produto):
        """Cadastra um produto na empresa."""
        self.produtos.append(produto)

    def alterar_quantidade(self, nome_produto, nova_quantidade):
        """Altera a quantidade disponível de um produto."""
        for p in self.produtos:
            if p.nome == nome_produto:
                p.quantidade = nova_quantidade
                return True
        return False

    def receber_pedido(self, pedido):
        """Recebe um pedido para análise."""
        self.pedido_recebido = pedido
        return f"Pedido {pedido.id} recebido para análise."

    def aceitar_pedido(self, pedido):
        """Aceita o pedido."""
        pedido.status = "Aceito"
        return f"Pedido {pedido.id} aceito."

    def rejeitar_pedido(self, pedido, motivo=""):
        """Rejeita o pedido."""
        pedido.status = "Rejeitado"
        pedido.motivo_rejeicao = motivo
        return f"Pedido {pedido.id} rejeitado. Motivo: {motivo}"

    def solicitar_ajuste(self, pedido, ajustes):
        """Solicita ajustes no pedido."""
        pedido.status = "Ajuste Solicitado"
        pedido.ajustes_solicitados = ajustes
        return f"Pedido {pedido.id}: ajuste solicitado."

    def atualizar_status_entrega(self, pedido, novo_status):
        """Atualiza o status de entrega do pedido."""
        pedido.status_entrega = novo_status
        return f"Status de entrega do pedido {pedido.id} atualizado para: {novo_status}"