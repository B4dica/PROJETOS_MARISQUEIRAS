import datetime

class Pedido:
    def __init__(self):
        self.id_pedido = None  # será definido externamente
        self.comprador = None  # EmpresaCompradora
        self.vendedor = None   # EmpresaMarisqueira
        self.itens = []        # lista de ItemPedido
        self.status_pedido = "Recebido"  # Recebido, Aceito, Rejeitado, Ajuste Solicitado, Em Preparo, Em Curso, Finalizado
        self.status_entrega = "Pendente"  # Pendente, Em Transporte, Entregue
        self.motivo_rejeicao = ""
        self.ajustes_solicitados = ""
        self.endereco_entrega = ""
        self.tempo_entrega = ""
        self.data_pedido = datetime.datetime.now()
        self.nota_avaliacao = None  # após entrega

    def receber_pedido(self):
        """Define o status como recebido (já é padrão ao criar)."""
        self.status_pedido = "Recebido"
        return f"Pedido {self.id_pedido} recebido."

    def aceitar_pedido(self):
        """Aceita o pedido."""
        self.status_pedido = "Aceito"
        return f"Pedido {self.id_pedido} aceito."

    def rejeitar_pedido(self, motivo=""):
        """Rejeita o pedido."""
        self.status_pedido = "Rejeitado"
        self.motivo_rejeicao = motivo
        return f"Pedido {self.id_pedido} rejeitado. Motivo: {motivo}"

    def solicitar_ajuste(self, ajustes):
        """Solicita ajustes no pedido."""
        self.status_pedido = "Ajuste Solicitado"
        self.ajustes_solicitados = ajustes
        return f"Pedido {self.id_pedido}: ajuste solicitado: {ajustes}"

    def atualizar_status_entrega(self, novo_status):
        """Atualiza o status de entrega."""
        self.status_entrega = novo_status
        return f"Status de entrega atualizado para: {novo_status}"

    def adicionar_item(self, produto, quantidade):
        """Adiciona um item ao pedido."""
        from ItemPedido import ItemPedido
        item = ItemPedido()
        item.id_pedido = self.id_pedido
        item.id_produto = produto.id_produto
        item.quantidade = quantidade
        self.itens.append(item)
        return item

    def validar_quantidade(self):
        """Valida quantidade mínima de 25 kg por item e disponibilidade."""
        for item in self.itens:
            # precisamos obter o produto para validar
            # Assumimos que o produto está acessível via alguma referência global ou através do vendedor
            # Para simplificação, vamos buscar no vendedor.produtos
            produto = None
            if self.vendedor:
                for p in self.vendedor.produtos:
                    if p.id_produto == item.id_produto:
                        produto = p
                        break
            if produto is None:
                return False, f"Produto com id {item.id_produto} não encontrado."
            valido, msg = produto.validar_quantidade(item.quantidade)
            if not valido:
                return False, f"Produto {produto.nome}: {msg}"
        return True, "Todos os itens válidos."

    def registrar_nota(self, nota, comentario=""):
        """Registra nota de avaliação após entrega."""
        if self.status_entrega.lower() == "entregue":
            self.nota_avaliacao = nota
            from Avaliacao import Avaliacao
            avaliacao = Avaliacao()
            avaliacao.id_avaliacao = len(self.vendedor.avaliacoes_recebidas) + 1 if self.vendedor and hasattr(self.vendedor, 'avaliacoes_recebidas') else 1
            avaliacao.nota = nota
            avaliacao.comentario = comentario
            avaliacao.pedido = self
            avaliacao.empresa_avaliada = self.vendedor
            avaliacao.empresa_avaliadora = self.comprador
            return avaliacao
        else:
            raise Exception("Somente pedidos entregues podem ser avaliados.")