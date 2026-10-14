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

if __name__ == "__main__":
    # exemplo de uso
    av = Avaliacao()
    av.registrar_nota(4, "Produto de boa qualidade")
    print("Avaliacao criada:")
    print(f"  ID: {av.id_avaliacao}")
    print(f"  Nota: {av.nota}")
    # comentário não armazenado, portanto não exibido
    # avaliar_empresa retorna a nota
    print(f"  avaliar_empresa() retorna: {av.avaliar_empresa()}")
    # testar nota inválida
    try:
        av.registrar_nota(6)
    except ValueError as e:
        print(f"\nErro ao registrar nota 6: {e}")