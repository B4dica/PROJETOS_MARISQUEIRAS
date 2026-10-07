class EmpresaCompradora:
    def __init__(self, id_empresa_compradora="", nome="", localizacao=""):
        self.id_empresa_compradora = id_empresa_compradora  # CNPJ
        self.nome = nome
        self.localizacao = localizacao
        self.pedidos_realizados = []  # lista de Pedido
        self.avaliacoes_dadas = []    # lista de Avaliacao

    def realizar_pedido(self, vendedor, produtos_quantidades, endereco_entrega, tempo_entrega):
        """Cria e realiza um pedido."""
        from Pedido import Pedido
        pedido = Pedido()
        pedido.id_pedido = len(self.pedidos_realizados) + 1  # simples incremental
        pedido.comprador = self
        pedido.vendedor = vendedor
        pedido.endereco_entrega = endereco_entrega
        pedido.tempo_entrega = tempo_entrega
        pedido.status_pedido = "Recebido"
        # valida quantidade mínima de 25kg por produto e disponibilidade
        for prod, qtd in produtos_quantidades.items():
            if qtd < 25:
                raise ValueError(f"Quantidade mínima de 25 kg não atingida para {prod.nome}")
            if prod.quantidade_disponivel < qtd:
                raise ValueError(f"Estoque insuficiente para {prod.nome}")
            from ItemPedido import ItemPedido
            item = ItemPedido()
            item.id_pedido = pedido.id_pedido
            item.id_produto = prod.id_produto
            item.quantidade = qtd
            pedido.itens.append(item)
        self.pedidos_realizados.append(pedido)
        # Notifica o vendedor
        vendedor.receber_pedido(pedido)
        return pedido

    def avaliar_empresa(self, vendedor, nota, comentario=""):
        """Avalia a empresa marisqueira após a compra."""
        from Avaliacao import Avaliacao
        avaliacao = Avaliacao()
        avaliacao.id_avaliacao = len(vendedor.avaliacoes_recebidas) + 1 if hasattr(vendedor, 'avaliacoes_recebidas') else 1
        avaliacao.nota = nota
        avaliacao.comentario = comentario
        avaliacao.empresa_avaliada = vendedor
        avaliacao.empresa_avaliadora = self
        self.avaliacoes_dadas.append(avaliacao)
        if hasattr(vendedor, 'avaliacoes_recebidas'):
            vendedor.avaliacoes_recebidas.append(avaliacao)
        else:
            vendedor.avaliacoes_recebidas = [avaliacao]
        return avaliacao

    def comparar_produtos(self, produtos):
        """Compara uma lista de produtos por preço (menor para maior)."""
        return sorted(produtos, key=lambda p: p.preco)

    def consultar_produtos(self, vendedores, nome=None, categoria=None, empresa=None, avaliacao_min=0):
        """Consulta produtos disponíveis nos vendedores fornecidos."""
        resultados = []
        for vendedor in vendedores:
            for prod in vendedor.produtos:
                if prod.quantidade_disponivel <= 0:
                    continue  # indisponível
                if nome and nome.lower() not in prod.nome.lower():
                    continue
                if categoria and prod.categoria != categoria:
                    continue
                if empresa and empresa.lower() not in vendedor.nome.lower():
                    continue
                # avaliação da empresa (média das notas)
                media = self._media_avaliacao(vendedor)
                if media < avaliacao_min:
                    continue
                resultados.append(prod)
        return resultados

    def verificar_disponibilidade(self, produto, quantidade):
        """Verifica se há quantidade suficiente em estoque."""
        return produto.quantidade_disponivel >= quantidade

    def _media_avaliacao(self, vendedor):
        if not hasattr(vendedor, 'avaliacoes_recebidas') or not vendedor.avaliacoes_recebidas:
            return 0
        soma = sum(a.nota for a in vendedor.avaliacoes_recebidas)
        return soma / len(vendedor.avaliacoes_recebidas)