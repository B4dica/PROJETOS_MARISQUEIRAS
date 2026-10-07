# IMPLEMENTAÇÃO POO - MARISQUEIRAS DA ILHA

## CLASSES, ATRIBUTOS E RESTRIÇÕES

**DOCENTE:** ALINE MAYA  
**DATA:** 07/10/2026

---

## 1. Classes e Atributos

### EMPRESA_MARISQUEIRA

| Atributo | Observação |
|----------|------------|
| id_empresa_marisqueira | CNPJ |
| nome | Nome da empresa. |
| localizacao | Localização usada como critério de consulta; a forma detalhada de armazenamento é uma decisão de modelagem. |

**Observação:** EMPRESA_MARISQUEIRA representa a empresa responsável pelo fornecimento dos produtos e pela entrega.

---

### EMPRESA_COMPRADORA

| Atributo | Observação |
|----------|------------|
| id_empresa_compradora | CNPJ |
| nome | Nome da empresa. |
| localizacao | Localização usada como critério de consulta; a forma detalhada de armazenamento é uma decisão de modelagem. |

**Observação:** Especialização de EMPRESA que representa a empresa que realiza as compras.

---

### PRODUTO

| Atributo | Observação |
|----------|------------|
| id_produto | Identificador do produto. |
| nome | Nome do produto. |
| categoria | Categoria: fresco ou congelado. |
| preco | Preço definido para o produto e a empresa. |
| quantidade_disponivel | Quantidade disponível para comercialização, em kg. |
| fotografia | Fotografia do produto; opcional. |

**Observação:** Fresco e congelado são cadastrados como produtos diferentes. Quando a quantidade chega a zero, o produto permanece cadastrado e aparece como indisponível.

---

### PEDIDO

| Atributo | Observação |
|----------|------------|
| id_pedido | Identificador do pedido. |
| endereco_entrega | Endereço para entrega. |
| tempo_entrega | Tempo de entrega informado no pedido. |
| status_pedido | Pedido em preparo, em curso (no caminho para entrega) e finalizado. |

**Observação:** Um pedido pode conter vários produtos, mas não pode reunir produtos de empresas das marisqueiras diferentes.

---

### ITEM_PEDIDO

| Atributo | Observação |
|----------|------------|
| id_pedido | Pedido ao qual o item pertence. |
| id_produto | Produto que participa do pedido. |
| quantidade | Quantidade solicitada do produto, em kg. |

**Observação:** É a entidade associativa entre PEDIDO e PRODUTO. A quantidade mínima é de 25 kg por produto e não pode ultrapassar a disponibilidade.

---

### AVALIACAO

| Atributo | Observação |
|----------|------------|
| id_avaliacao | Identificador da avaliação. |
| nota | Nota de 1 a 5 estrelas. |

**Observação:** O requisito informa a escala de 1 a 5 estrelas, mas não define a cardinalidade exata das avaliações.

---

## 3. Restrições

- A quantidade mínima de comercialização é de 25 kg para cada produto.
- A quantidade solicitada não pode ultrapassar a quantidade disponível.
- Um pedido pode conter vários produtos, mas todos devem pertencer à mesma EMPRESA_MARISQUEIRA.
- Não existe valor financeiro mínimo para o pedido.
- Quando o estoque de um produto chega a zero, o produto permanece cadastrado como indisponível.
- A forma de pagamento está fora do escopo atual.
- A entrega é realizada pela própria EMPRESA_MARISQUEIRA, sem rastreamento em tempo real.