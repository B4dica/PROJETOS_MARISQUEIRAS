Métodos implementados por classe – Projeto *Marisqueiras da Ilha*  

**Empresa**
• Métodos (assinatura resumida): __init__(self, nome="", cnpj="") <br> cadastrar_produto(self, produto) <br> alterar_quantidade(self, nome_produto, nova_quantidade) <br> receber_pedido(self, pedido) <br> aceitar_pedido(self, pedido) <br> rejeitar_pedido(self, pedido, motivo="") <br> solicitar_ajuste(self, pedido, ajustes) <br> atualizar_status_entrega(self, pedido, novo_status)

**EmpresaMarisqueira**
• Métodos (assinatura resumida): def __init__(self, nome="", cnpj=""): (herda de Empresa) <br> não adiciona novos métodos além dos herdados

**EmpresaCompradora**
• Métodos (assinatura resumida): __init__(self, nome="", cnpj="") <br> realizar_pedido(self, vendedor, produtos_quantidades, endereco_entrega, tempo_entrega) <br> avaliar_empresa(self, vendedor, nota, comentario="") <br> comparar_produtos(self, produtos) <br> consultar_produtos(self, vendedores, nome=None, categoria=None, empresa=None, avaliacao_min=0) <br> verificar_disponibilidade(self, produto, quantidade) <br> _media_avaliacao(self, vendedor) (método auxiliar privado)

**Produto**
• Métodos (assinatura resumida): __init__(self, nome="", categoria="", preco=0.0, quantidade=0, empresa=None) <br> cadastrar_produto(self, nome, categoria, preco, quantidade, empresa) <br> alterar_quantidade(self, nova_quantidade) <br> atualizar_quantidade(self, quantidade_adicional) <br> validar_quantidade(self, quantidade_solicitada)

**Pedido**
• Métodos (assinatura resumida): __init__(self) <br> receber_pedido(self) <br> aceitar_pedido(self) <br> rejeitar_pedido(self, motivo="") <br> solicitar_ajuste(self, ajustes) <br> atualizar_status_entrega(self, novo_status) <br> adicionar_item(self, produto, quantidade) <br> validar_quantidade(self) <br> registrar_nota(self, nota, comentario="")

**ItemPedido**
• Métodos (assinatura resumida): __init__(self) <br> adicionar_item(self, produto, quantidade) <br> validar_quantidade(self)

**Avaliacao**
• Métodos (assinatura resumida): __init__(self) <br> registrar_nota(self, nota, comentario="") <br> avaliar_empresa(self)

---