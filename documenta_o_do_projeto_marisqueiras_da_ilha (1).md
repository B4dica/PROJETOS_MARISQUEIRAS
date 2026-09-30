# Documentação do Projeto: Marisqueiras da Ilha
**Docente:** Aline Maya  
**Data:** 30/09/2026  
**Instituição:** UNDB — Centro Universitário  
**Programa:** Aprendizagem Baseada em Projetos (PjBL)

---

## Parte 1: Atividade de POO — Implementação de Classes e Métodos

### Tarefa
Implementar os métodos de acordo com os requisitos, critérios e regras de negócio do projeto **Marisqueiras da Ilha**, fornecidos pela professora.

### Classes Envolvidas
* `Empresa`
* `EmpresaMarisqueira`
* `EmpresaCompradora`
* `Produto`
* `Pedido`
* `ItemPedido`
* `Avaliacao`

### Métodos a Implementar
* `cadastrar_produto()`
* `alterar_quantidade()`
* `receber_pedido()`
* `aceitar_pedido()`
* `rejeitar_pedido()`
* `solicitar_ajuste()`
* `atualizar_status_entrega()`
* `consultar_produtos()`
* `comparar_produtos()`
* `realizar_pedido()`
* `avaliar_empresa()`
* `verificar_disponibilidade()`
* `atualizar_quantidade()`
* `adicionar_item()`
* `validar_quantidade()`
* `registrar_nota()`

---

## Parte 2: Documento-Base de Requisitos do Projeto

### Caracterização do Projeto

| ID | Pergunta | Resposta |
|:---|:---|:---|
| P1 | Qual é o nome do projeto? | Marisqueiras da Ilha. |
| P2 | Qual é o objetivo da implementação? | Desenvolver uma solução digital para apoiar a comercialização direta de mariscos entre empresas das marisqueiras e empresas compradoras, organizando a oferta, a consulta de produtos, os pedidos, o fornecimento e a entrega. A rastreabilidade, a origem, a qualidade e a procedência ficam como possibilidade futura. |
| P3 | Qual é o problema que originou o projeto? | As marisqueiras enfrentam dificuldade para realizar vendas diretas, com dependência de intermediários, ausência de mecanismos comerciais formais e dificuldade de acesso ao mercado. |
| P4 | Qual comunidade está relacionada ao projeto? | Vila Maresia, em Raposa, Maranhão, é o caso inicial de estudo. O projeto pretende futuramente atender outras comunidades. |
| P5 | Qual é o modelo de negócio do projeto? | B2B (empresa para empresa). |
| P6 | O projeto atende consumidor final ou empresas? | Atende somente empresas. Não é destinado ao consumidor final. As compras são realizadas em maiores quantidades. |
| P7 | Qual é o fluxo básico da comercialização? | A empresa compradora consulta os produtos, seleciona o produto, realiza o pedido, a empresa das marisqueiras recebe e analisa o pedido, podendo aceitar, rejeitar ou solicitar ajuste. Após a preparação, ocorre a entrega ao comprador. |
| P8 | O que é a plataforma dentro do projeto? | A solução atual é o aplicativo Marisquês. Não há uma solução web separada neste momento. |
| P9 | Como a empresa compradora encontra os produtos? | A busca considera nome do produto, categoria (fresco/congelado), localização, empresa/marisqueira e avaliação em estrelas. Também há filtros e opções de ordenação. |
| P10 | Quem participa diretamente da operação da plataforma? | Participam diretamente a empresa das marisqueiras e a empresa compradora. A entrega é realizada pela própria empresa das marisqueiras. O custo da entrega está incorporado ao preço do produto. O aplicativo permite informar e atualizar o status da entrega, sem rastreamento em tempo real. |
| P11 | Como uma habitação é cadastrada no aplicativo? | A comunidade é formada por habitações, e cada habitação corresponde a uma empresa. A organização interna da família não é gerenciada pela plataforma. |
| P12 | Uma marisqueira pode atuar individualmente como empresa? | Uma pessoa por habitação realiza o cadastro da empresa e fica responsável pelo acesso. |
| P13 | (Atuação individual) | Sim. Uma marisqueira pode atuar individualmente como empresa desde que consiga atender à capacidade necessária para as condições comerciais da plataforma. |
| P14 | Como a família divide seus valores e atividades? | A divisão interna de valores, responsabilidades e atividades da família não é gerenciada pela plataforma. |

---

### Produtos e Consulta

| ID | Pergunta | Resposta |
|:---|:---|:---|
| P15 | Quais dados são obrigatórios para cadastrar um produto? | Todos os dados são obrigatórios, exceto a foto. |
| P16 | Qual é a unidade de venda dos produtos? | A unidade de venda é o quilograma (kg). A quantidade mínima é de 25 kg. |
| P17 | O preço é definido por produto e empresa? Existem regras para alteração? | O preço é definido por produto e empresa. O preço não pode ser alterado durante uma venda. |
| P18 | A empresa pode cadastrar o mesmo produto mais de uma vez, como fresco e congelado? | Sim. Produto fresco e produto congelado são cadastrados como produtos diferentes. A busca pode ser filtrada pela categoria. |
| P19 | A quantidade disponível precisa ser informada no cadastro? Ela pode ser alterada? | A quantidade disponível precisa ser informada. Deve atender ao mínimo definido de 25 kg e pode ser alterada a qualquer momento pela pessoa responsável pela empresa. |
| P20 | Quando a quantidade disponível chega a zero, o que acontece com o produto? | O produto continua aparecendo como indisponível. |
| P21 | Quais filtros estarão disponíveis na busca? | Categoria (fresco/congelado), localização, empresa/marisqueira e avaliação em estrelas. Não haverá outros filtros. |
| P22 | O comprador poderá ordenar os resultados? | Sim. Poderá ordenar por menor preço, maior preço, melhor avaliação e proximidade/localização. |
| P23 | A avaliação em estrelas será dada por quem? | A empresa compradora avaliará a empresa das marisqueiras após a compra. |
| P24 | Qual será a escala da avaliação? | De 1 a 5 estrelas. |
| P25 | Uma empresa poderá ver produtos de outras empresas? | A empresa das marisqueiras visualiza apenas os próprios produtos. |
| P26 | O comprador poderá comparar produtos de empresas diferentes? | Sim. |

---

### Pedidos e Disponibilidade

| ID | Pergunta | Resposta |
|:---|:---|:---|
| P27 | Quais dados são obrigatórios para realizar um pedido? | Perfil da empresa compradora, produto, quantidade, endereço de entrega e tempo de entrega. A forma de pagamento foi definida para ficar fora dos requisitos neste momento. |
| P28 | Um pedido pode ter mais de um produto? | Sim. Um pedido pode conter mais de um produto. |
| P29 | Um pedido pode reunir produtos de empresas diferentes? | Não. As compras são individuais; um pedido não reúne produtos de empresas diferentes. |
| P30 | A quantidade mínima de 25 kg é aplicada para cada produto ou para o pedido inteiro? | Para cada produto. |
| P31 | Existe algum valor mínimo em dinheiro para realizar um pedido? | Não. O requisito mínimo é definido por quantidade, sendo 25 kg por produto. |
| P32 | Existe quantidade máxima que pode ser solicitada em um pedido? | Não existe quantidade máxima fixa. O limite é a quantidade disponível para venda. |
| P33 | A empresa das marisqueiras precisa ter capacidade mínima de fornecimento para permanecer cadastrada? | A empresa pode permanecer cadastrada mesmo sem estoque disponível. O aplicativo apresenta um indicador visual de situação: verde para disponível, laranja para estoque baixo e vermelho para fora do horário de funcionamento. |
| P34 | O que acontece quando a empresa compradora solicita uma quantidade maior do que a disponível? | O sistema impede o pedido e informa que aquela quantidade não está disponível. |

---

## Parte 3: Tabela Consolidada de Critérios

| ID | Tema | Critério |
|:---|:---|:---|
| P1 | Identificação | Nome do projeto: Marisqueiras da Ilha. |
| P2 | Objetivo | Apoiar a comercialização direta de mariscos entre empresas das marisqueiras e empresas compradoras, organizando a oferta, a consulta de produtos, os pedidos, o fornecimento e a entrega. |
| P3 | Problema | Dificuldade de venda direta, dependência de intermediários, ausência de mecanismos comerciais formais e dificuldade de acesso ao mercado. |
| P4 | Abrangência | Vila Maresia é o caso inicial; o projeto poderá atender outras comunidades futuramente. |
| P5 | Modelo de negócio | B2B. |
| P6 | Público-alvo | Somente empresas compradoras; não atende consumidor final. |
| P7 | Fluxo comercial | Consulta → seleção → pedido → análise pela empresa das marisqueiras → aceite, rejeição ou ajuste → preparação → entrega. |
| P8 | Aplicativo | A solução atual é o aplicativo Marisquês; não há solução web separada neste momento. |
| P9 | Consulta de produtos | Busca por nome, categoria, localização, empresa/marisqueira e avaliação em estrelas; há filtros e ordenação. |
| P10 | Participantes da operação | Empresa das marisqueiras e empresa compradora. A entrega é feita pela própria empresa das marisqueiras. |
| P11 | Organização | 1 habitação = 1 empresa. A organização interna da família não é gerenciada pelo aplicativo. |
| P12 | Cadastro da habitação | Uma pessoa por habitação cadastra a empresa e responde pelo acesso. |
| P13 | Atuação individual | Uma marisqueira pode atuar individualmente como empresa, desde que atenda às condições comerciais. |
| P14 | Organização familiar | Não é gerenciada pela plataforma. |
| P15 | Cadastro de produto | Todos os campos são obrigatórios, exceto a foto. |
| P16 | Unidade e quantidade mínima | Venda por kg; mínimo de 25 kg. |
| P17 | Preço | Preço definido por produto e empresa; não pode ser alterado durante uma venda. |
| P18 | Fresco/congelado | São produtos diferentes no cadastro e podem ser filtrados por categoria. |
| P19 | Estoque | A quantidade disponível é informada e pode ser alterada pela pessoa responsável pela empresa. O mínimo comercial é de 25 kg. |
| P20 | Estoque zerado | O produto permanece visível como indisponível. |
| P21 | Filtros | Categoria, localização, empresa/marisqueira e avaliação em estrelas. |
| P22 | Ordenação | Menor preço, maior preço, melhor avaliação e proximidade/localização. |
| P23 | Avaliação | A empresa compradora avalia a empresa das marisqueiras após a compra. |
| P24 | Escala | 1 a 5 estrelas. |
| P25 | Visibilidade da empresa | A empresa das marisqueiras visualiza somente os próprios produtos. |
| P26 | Comparação | A empresa compradora pode comparar produtos de empresas diferentes. |
| P27 | Dados obrigatórios do pedido | Perfil da empresa compradora, produto, quantidade, endereço de entrega e tempo de entrega. Pagamento fica fora do escopo atual. |
| P28 | Itens no pedido | Um pedido pode conter mais de um produto. |
| P29 | Empresas no pedido | Um pedido não pode reunir produtos de empresas diferentes. |
| P30 | Mínimo por produto | 25 kg para cada produto do pedido. |
| P31 | Valor mínimo | Não há valor financeiro mínimo; o requisito mínimo é de 25 kg por produto. |
| P32 | Quantidade máxima | Não há quantidade máxima fixa; a quantidade solicitada é limitada ao estoque disponível. |
| P33 | Status da empresa | A empresa permanece cadastrada mesmo sem estoque. Indicadores: verde — disponível; laranja — estoque baixo; vermelho — fora do horário de funcionamento. |
| P34 | Quantidade indisponível | Se a quantidade solicitada for maior que a disponível, o sistema impede o pedido e informa a indisponibilidade. |

---

## Parte 4: Regras de Negócio do Caso

| ID | Regra de Negócio |
|:---|:---|
| **RN01** | A comercialização ocorre entre empresas, no modelo B2B; não há atendimento ao consumidor final. |
| **RN02** | Cada habitação corresponde a uma empresa na representação do projeto. |
| **RN03** | Uma marisqueira pode atuar individualmente como empresa, desde que atenda às condições comerciais da plataforma. |
| **RN04** | Os produtos são comercializados por quilograma. |
| **RN05** | A quantidade mínima de comercialização é de 25 kg para cada produto. |
| **RN06** | Produto fresco e produto congelado são cadastrados como produtos diferentes. |
| **RN07** | O preço é definido por produto e empresa e não pode ser alterado durante uma venda. |
| **RN08** | A quantidade disponível do produto deve ser informada e pode ser alterada pela pessoa responsável pela empresa. |
| **RN09** | Quando a quantidade disponível de um produto chega a zero, o produto permanece cadastrado como indisponível. |
| **RN10** | A empresa compradora pode pesquisar produtos por nome, categoria, localização, empresa ou marisqueira e avaliação em estrelas. |
| **RN11** | Os resultados da busca podem ser ordenados por menor preço, maior preço, melhor avaliação e proximidade ou localização. |
| **RN12** | A empresa das marisqueiras visualiza apenas os próprios produtos; a empresa compradora pode visualizar e comparar produtos de empresas diferentes. |
| **RN13** | Um pedido deve registrar a empresa compradora, o produto ou produtos, a quantidade, o endereço de entrega e o tempo de entrega. A forma de pagamento está fora do escopo atual. |
| **RN14** | Um pedido pode conter vários produtos, mas não pode reunir produtos de empresas das marisqueiras diferentes. |
| **RN15** | A quantidade mínima de 25 kg é aplicada individualmente a cada produto do pedido. |
| **RN16** | Não existe valor financeiro mínimo para o pedido. |
| **RN17** | Não existe quantidade máxima fixa; a quantidade solicitada é limitada pela disponibilidade do produto. |
| **RN18** | Se a quantidade solicitada for maior que a disponível, o sistema deve impedir o pedido e informar a indisponibilidade. |
| **RN19** | A empresa das marisqueiras permanece cadastrada mesmo sem estoque disponível. |
| **RN20** | A situação visual da empresa pode indicar disponibilidade, estoque baixo ou fora do horário de funcionamento. |
| **RN21** | Após a compra, a empresa compradora pode avaliar a empresa das marisqueiras em uma escala de 1 a 5 estrelas. |
| **RN22** | A entrega é realizada pela própria empresa das marisqueiras; o aplicativo permite atualizar seu status, sem rastreamento em tempo real. |
| **RN23** | O custo da entrega está incorporado ao preço do produto. |
