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

if __name__ == "__main__":
    # exemplo de uso
    ped = Pedido()
    ped.id_pedido = 1001  # simulando definição externa
    ped.endereco_entrega = "Rua das Flores, 123"
    ped.tempo_entrega = "2 dias"
    print("Pedido criado:")
    print(f"  ID: {ped.id_pedido}")
    print(f"  Endereço de entrega: {ped.endereco_entrega}")
    print(f"  Tempo de entrega: {ped.tempo_entrega}")
    print(f"  Status inicial: {ped.status_pedido}")
    # receber_pedido (já está como Recebido, mas chamar para demonstrar)
    print("\nChamar receber_pedido():")
    print(ped.receber_pedido())
    print(f"  Status agora: {ped.status_pedido}")
    # aceitar_pedido
    print("\nChamar aceitar_pedido():")
    print(ped.aceitar_pedido())
    print(f"  Status agora: {ped.status_pedido}")
    # rejeitar_pedido
    print("\nChamar rejeitar_pedido('Sem estoque'):")
    print(ped.rejeitar_pedido("Sem estoque"))
    print(f"  Status agora: {ped.status_pedido}")
    # solicitar_ajuste
    print("\nChamar solicitar_ajuste('Reduzir quantidade'):")
    print(ped.solicitar_ajuste("Reduzir quantidade"))
    print(f"  Status agora: {ped.status_pedido}")