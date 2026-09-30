class Avaliacao:
    def __init__(self):
        self.nota = 0  # 1 a 5
        self.comentario = ""
        self.empresa_avaliada = None  # EmpresaMarisqueira
        self.empresa_avaliadora = None  # EmpresaCompradora
        self.pedido = None  # Pedido relacionado
        self.data = None

    def registrar_nota(self, nota, comentario=""):
        """Registra a nota e comentário."""
        if not (1 <= nota <= 5):
            raise ValueError("Nota deve estar entre 1 e 5.")
        self.nota = nota
        self.comentario = comentario
        self.data = __import__('datetime').datetime.now()
        return self

    def avaliar_empresa(self):
        """Retorna a média de avaliações da empresa avaliada (deve ser chamado na empresa)."""
        # Este método faz mais sentido na classe Empresa, mas aqui retornamos a nota desta avaliação.
        return self.nota