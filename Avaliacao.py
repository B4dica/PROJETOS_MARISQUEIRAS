class Avaliacao:
    def __init__(self):
        self.id_avaliacao = None  # Identificador da avaliação
        self.nota = 0             # Nota de 1 a 5 estrelas

    def registrar_nota(self, nota, comentario=""):
        """Registra a nota (comentário ignorado conforme atributos especificados)."""
        if not (1 <= nota <= 5):
            raise ValueError("Nota deve estar entre 1 e 5.")
        self.nota = nota
        # comentário e outros atributos não fazem parte da especificação
        return self

    def avaliar_empresa(self):
        """Retorna a nota desta avaliação (média seria calculada na empresa)."""
        return self.nota