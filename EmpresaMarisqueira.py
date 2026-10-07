class EmpresaMarisqueira:
    def __init__(self, id_empresa_marisqueira="", nome="", localizacao=""):
        self.id_empresa_marisqueira = id_empresa_marisqueira  # CNPJ
        self.nome = nome
        self.localizacao = localizacao
        self.produtos = []          # lista de Produto
        self.avaliacoes_recebidas = []  # lista de Avaliacao recebidas

    def cadastrar_produto(self, produto):
        """Adiciona um produto à lista de produtos da empresa."""
        self.produtos.append(produto)

    def alterar_quantidade(self, nome_produto, nova_quantidade):
        """Altera a quantidade disponível de um produto."""
        for p in self.produtos:
            if p.nome == nome_produto:
                p.quantidade_disponivel = nova_quantidade
                return True
        return False

    def receber_pedido(self, pedido):
        """Recebe um pedido para análise."""
        self.pedido_recebido = pedido
        return f"Pedido {pedido.id_pedido} recebido para análise."

    def aceitar_pedido(self, pedido):
        """Aceita o pedido."""
        pedido.status_pedido = "Aceito"
        return f"Pedido {pedido.id_pedido} aceito."

    def rejeitar_pedido(self, pedido, motivo=""):
        """Rejeita o pedido."""
        pedido.status_pedido = "Rejeitado"
        pedido.motivo_rejeicao = motivo
        return f"Pedido {pedido.id_pedido} rejeitado. Motivo: {motivo}"

    def solicitar_ajuste(self, pedido, ajustes):
        """Solicita ajustes no pedido."""
        pedido.status_pedido = "Ajuste Solicitado"
        pedido.ajustes_solicitados = ajustes
        return f"Pedido {pedido.id_pedido}: ajuste solicitado."

    def atualizar_status_entrega(self, pedido, novo_status):
        """Atualiza o status de entrega do pedido."""
        pedido.status_entrega = novo_status
        return f"Status de entrega do pedido {pedido.id_pedido} atualizado para: {novo_status}"