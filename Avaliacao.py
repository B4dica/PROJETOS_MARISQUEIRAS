class Avaliacao:
    def __init__(self):
        self.id_avaliacao = None  # Identificador da avaliação
        self.nota = 0             # Nota de 1 a 5 estrelas
        self.comentario = ""
        self.empresa_avaliada = None  # EmpresaMarisqueira
        self.empresa_avaliadora = None  # EmpresaCompradora
        self.pedido = None        # Pedido relacionado
        self.data = None

    def registrar_nota(self, nota, comentario=""):
        """Registra a nota e comentário."""
        if not (1 <= nota <= 5):
            raise ValueError("Nota deve estar entre 1 e 5.")
        self.nota = nota
        self.comentario = comentario
        # opcional: definir data
        # from datetime import datetime
        # self.data = datetime.now()
        return self

    def avaliar_empresa(self):
        """Retorna a nota desta avaliação (média seria calculada na empresa)."""
        return self.nota