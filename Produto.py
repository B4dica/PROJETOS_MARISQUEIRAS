class Produto:
    _next_id = 1  # contador simples para gerar IDs únicos

    def __init__(self, id_produto="", nome="", categoria="", preco=0.0, quantidade_disponivel=0, fotografia=None):
        if id_produto:
            self.id_produto = id_produto
        else:
            self.id_produto = str(Produto._next_id)
            Produto._next_id += 1
        self.nome = nome
        self.categoria = categoria.lower()  # fresco ou congelado
        self.preco = preco  # preço por kg
        self.quantidade_disponivel = quantidade_disponivel  # estoque disponível em kg
        self.fotografia = fotografia  # opcional, não obrigatório conforme RN

    def cadastrar_produto(self, nome, categoria, preco, quantidade_disponivel, fotografia=None):
        """Define os atributos do produto."""
        self.nome = nome
        self.categoria = categoria.lower()
        self.preco = preco
        self.quantidade_disponivel = quantidade_disponivel
        self.fotografia = fotografia
        # garante que tenha um ID
        if not self.id_produto:
            self.id_produto = str(Produto._next_id)
            Produto._next_id += 1
        return self

    def alterar_quantidade(self, nova_quantidade):
        """Altera a quantidade disponível (em kg)."""
        if nova_quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.quantidade_disponivel = nova_quantidade

    def atualizar_quantidade(self, quantidade_adicional):
        """Adiciona ou subtrai quantidade no estoque."""
        nova_qtd = self.quantidade_disponivel + quantidade_adicional
        if nova_qtd < 0:
            raise ValueError("Estoque não pode ficar negativo.")
        self.quantidade_disponivel = nova_qtd

    def validar_quantidade(self, quantidade_solicitada):
        """Verifica se a quantidade solicitada é válida (mínimo 25 kg e disponível)."""
        if quantidade_solicitada < 25:
            return False, "Quantidade mínima de 25 kg não atingida."
        if quantidade_solicitada > self.quantidade_disponivel:
            return False, "Estoque insuficiente."
        return True, "Quantidade válida."

if __name__ == "__main__":
    # exemplo de uso
    prod = Produto()
    print("Produto criado (ID gerado automaticamente):", prod.id_produto)
    # cadastrar produto
    prod.cadastrar_produto(nome="Camarão", categoria="fresco", preco=50.0, quantidade_disponivel=100)
    print("\nApós cadastrar_produto:")
    print(f"  Nome: {prod.nome}")
    print(f"  Categoria: {prod.categoria}")
    print(f"  Preço: {prod.preco}")
    print(f"  Quantidade disponível: {prod.quantidade_disponivel}")
    print(f"  Fotografia: {prod.fotografia}")
    # alterar quantidade
    prod.alterar_quantidade(80)
    print("\nApós alterar_quantidade(80):")
    print(f"  Quantidade disponível: {prod.quantidade_disponivel}")
    # atualizar quantidade (adicionar 20)
    prod.atualizar_quantidade(20)
    print("\nApós atualizar_quantidade(+20):")
    print(f"  Quantidade disponível: {prod.quantidade_disponivel}")
    # validar quantidade
    valido, msg = prod.validar_quantidade(30)
    print("\nValidar quantidade 30 kg:")
    print(f"  Válido: {valido}, Mensagem: {msg}")
    valido, msg = prod.validar_quantidade(200)
    print("\nValidar quantidade 200 kg (deve falhar):")
    print(f"  Válido: {valido}, Mensagem: {msg}")
    valido, msg = prod.validar_quantidade(20)
    print("\nValidar quantidade 20 kg (<25):")
    print(f"  Válido: {valido}, Mensagem: {msg}")