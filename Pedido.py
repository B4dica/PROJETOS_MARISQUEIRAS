from ItemPedido import ItemPedido
import datetime

class Pedido:
    def __init__(self):
        self.id = None  # pode ser definido externamente
        self.comprador = None  # EmpresaCompradora
        self.vendedor = None   # EmpresaMarisqueira
        self.itens = []        # lista de ItemPedido
        self.status = "Recebido"  # Recebido, Aceito, Rejeitado, Ajuste Solicitado, Preparado, Entregue
        self.status_entrega = "Pendente"  # Pendente, Em Transporte, Entregue
        self.motivo_rejeicao = ""
        self.ajustes_solicitados = ""
        self.data_pedido = datetime.datetime.now()
        self.nota_avaliacao = None  # após entrega

    def receber_pedido(self):
        """Define o status como recebido (já é padrão ao criar)."""
        self.status = "Recebido"
        return f"Pedido {self.id} recebido."

    def aceitar_pedido(self):
        """Aceita o pedido."""
        self.status = "Aceito"
        return f"Pedido {self.id} aceito."

    def rejeitar_pedido(self, motivo=""):
        """Rejeita o pedido."""
        self.status = "Rejeitado"
        self.motivo_rejeicao = motivo
        return f"Pedido {self.id} rejeitado. Motivo: {motivo}"

    def solicitar_ajuste(self, ajustes):
        """Solicita ajustes no pedido."""
        self.status = "Ajuste Solicitado"
        self.ajustes_solicitados = ajustes
        return f"Pedido {self.id}: ajuste solicitado: {ajustes}"

    def atualizar_status_entrega(self, novo_status):
        """Atualiza o status de entrega."""
        self.status_entrega = novo_status
        return f"Status de entrega atualizado para: {novo_status}"

    def adicionar_item(self, produto, quantidade):
        """Adiciona um item ao pedido."""
        item = ItemPedido()
        item.produto = produto
        item.quantidade = quantidade
        self.itens.append(item)
        return item

    def validar_quantidade(self):
        """Valida quantidade mínima de 25 kg por item e disponibilidade."""
        for item in self.itens:
            valido, msg = item.produto.validar_quantidade(item.quantidade)
            if not valido:
                return False, f"Produto {item.produto.nome}: {msg}"
        return True, "Todos os itens válidos."

    def registrar_nota(self, nota, comentario=""):
        """Registra nota de avaliação após entrega."""
        if self.status_entrega.lower() == "entregue":
            self.nota_avaliacao = nota
            # Também pode criar uma Avaliacao e associar
            from Avaliacao import Avaliacao
            avaliacao = Avaliacao()
            avaliacao.nota = nota
            avaliacao.comentario = comentario
            avaliacao.pedido = self
            avaliacao.empresa_avaliada = self.vendedor
            avaliacao.empresa_avaliadora = self.comprador
            return avaliacao
        else:
            raise Exception("Somente pedidos entregues podem ser avaliados.")