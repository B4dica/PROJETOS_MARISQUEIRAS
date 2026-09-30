from ItemPedido import ItemPedido

class EmpresaCompradora:
    def __init__(self, nome="", cnpj=""):
        self.nome = nome
        self.cnpj = cnpj
        self.pedidos_realizados = []  # list of Pedido objects
        self.avaliacoes_dadas = []    # list of Avaliacao objects

    def realizar_pedido(self, vendedor, produtos_quantidades, endereco_entrega, tempo_entrega):
        """
        Cria e realiza um pedido.
        vendedor: objeto EmpresaMarisqueira
        produtos_quantidades: dict {Produto: quantidade}
        """
        from Pedido import Pedido
        pedido = Pedido()
        pedido.comprador = self
        pedido.vendedor = vendedor
        pedido.endereco_entrega = endereco_entrega
        pedido.tempo_entrega = tempo_entrega
        # valida quantidade mínima de 25kg por produto
        for prod, qtd in produtos_quantidades.items():
            if qtd < 25:
                raise ValueError(f"Quantidade mínima de 25 kg não atingida para {prod.nome}")
            if prod.quantidade < qtd:
                raise ValueError(f"Estoque insuficiente para {prod.nome}")
            item = ItemPedido()
            item.produto = prod
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
        avaliacao.nota = nota
        avaliacao.comentario = comentario
        avaliacao.empresa_avaliada = vendedor
        avaliacao.empresa_avaliadora = self
        self.avaliacoes_dadas.append(avaliacao)
        vendedor.avaliacoes_recebidas.append(avaliacao)
        return avaliacao

    def comparar_produtos(self, produtos):
        """
        Compara uma lista de produtos (de diferentes vendedores) por preço, avaliação, etc.
        produtos: lista de Produto
        Retorna lista ordenada por preço crescente.
        """
        return sorted(produtos, key=lambda p: p.preco)

    def consultar_produtos(self, vendedores, nome=None, categoria=None, empresa=None, avaliacao_min=0):
        """
        Consulta produtos disponíveis nos vendedores fornecidos.
        vendedores: lista de EmpresaMarisqueira
        Filtros opcionais: nome (str), categoria ('fresco'/'congelado'), empresa (nome), avaliacao_min (int)
        Retorna lista de Produto que atendem aos filtros.
        """
        resultados = []
        for vendedor in vendedores:
            for prod in vendedor.produtos:
                if prod.quantidade <= 0:
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
        return produto.quantidade >= quantidade

    def _media_avaliacao(self, vendedor):
        if not hasattr(vendedor, 'avaliacoes_recebidas') or not vendedor.avaliacoes_recebidas:
            return 0
        soma = sum(a.nota for a in vendedor.avaliacoes_recebidas)
        return soma / len(vendedor.avaliacoes_recebidas)