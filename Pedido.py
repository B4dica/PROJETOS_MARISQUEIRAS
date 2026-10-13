
class Pedido:
    def __init__(self):
        self.id_pedido = None  # será definido externamente
        self.endereco_entrega = ""
        self.tempo_entrega = ""
        self.status_pedido = "Recebido"  # Recebido, Aceito, Rejeitado, Ajuste Solicitado, Em Preparo, Em Curso, Finalizado

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
        # motivo ignorado conforme atributos especificados
        return f"Pedido {self.id_pedido} rejeitado."

    def solicitar_ajuste(self, ajustes):
        """Solicita ajustes no pedido."""
        self.status_pedido = "Ajuste Solicitado"
        # ajustes ignorado conforme atributos especificados
        return f"Pedido {self.id_pedido}: ajuste solicitado."