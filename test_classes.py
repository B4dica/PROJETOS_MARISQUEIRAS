import sys
sys.path.append(r'C:\Users\garci\OneDrive\Área de Trabalho\Exercícios(POO30_09)')
from Empresa import Empresa
from EmpresaMarisqueira import EmpresaMarisqueira
from EmpresaCompradora import EmpresaCompradora
from Produto import Produto
from Pedido import Pedido
from ItemPedido import ItemPedido
from Avaliacao import Avaliacao
import pytest

def test_produto_cadastro_e_estoque():
    emp = EmpresaMarisqueira('Marisqueira Teste', '00.000.000/0001-00')
    prod = Produto()
    prod.cadastrar_produto('Camarão', 'fresco', 50.0, 100, emp)
    emp.cadastrar_produto(prod)
    assert prod.nome == 'Camarão'
    assert prod.quantidade == 100
    assert prod.preco == 50.0
    # test validar quantidade
    valido, msg = prod.validar_quantidade(30)
    assert valido == True
    valido, msg = prod.validar_quantidade(20)
    assert valido == False
    assert 'mínima' in msg.lower()
    # test alterar quantidade
    prod.alterar_quantidade(80)
    assert prod.quantidade == 80

def test_pedido_fluxo():
    emp_v = EmpresaMarisqueira('Vendedor', '111')
    emp_c = EmpresaCompradora('Comprador', '222')
    prod = Produto()
    prod.cadastrar_produto('Siri', 'congelado', 40.0, 50, emp_v)
    emp_v.cadastrar_produto(prod)
    pedido = emp_c.realizar_pedido(emp_v, {prod: 30}, 'Endereco X', '1 dia')
    assert pedido.status == 'Recebido'
    assert len(pedido.itens) == 1
    assert pedido.itens[0].quantidade == 30
    # aceitar
    emp_v.aceitar_pedido(pedido)
    assert pedido.status == 'Aceito'
    # rejeitar motivo - test that quantity <25 raises ValueError
    with pytest.raises(ValueError, match='Quantidade mínima de 25 kg'):
        emp_c.realizar_pedido(emp_v, {prod: 10}, 'Endereco Y', '2 dias')
    # valid pedido with sufficient quantity
    pedido2 = emp_c.realizar_pedido(emp_v, {prod: 30}, 'Endereco Y', '2 dias')
    emp_v.rejeitar_pedido(pedido2, 'Sem condições')
    assert pedido2.status == 'Rejeitado'
    assert pedido2.motivo_rejeicao == 'Sem condições'
    # ajuste
    pedido3 = emp_c.realizar_pedido(emp_v, {prod: 30}, 'Endereco Z', '3 dias')
    emp_v.solicitar_ajuste(pedido3, 'Reduzir para 15kg')
    assert pedido3.status == 'Ajuste Solicitado'
    assert pedido3.ajustes_solicitados == 'Reduzir para 15kg'
    # atualizar status entrega
    emp_v.atualizar_status_entrega(pedido3, 'Em Transporte')
    assert pedido3.status_entrega == 'Em Transporte'
    emp_v.atualizar_status_entrega(pedido3, 'Entregue')
    assert pedido3.status_entrega == 'Entregue'

def test_avaliacao():
    emp_v = EmpresaMarisqueira('Avaliando', '333')
    emp_c = EmpresaCompradora('Avaliador', '444')
    aval = Avaliacao()
    aval.registrar_nota(4, 'Bom')
    assert aval.nota == 4
    assert aval.comentario == 'Bom'
    # test avaliar_empresa method (just returns nota)
    assert aval.avaliar_empresa() == 4
    # test media via EmpresaCompradora
    emp_v.avaliacoes_recebidas.append(aval)
    emp_v.avaliacoes_recebidas.append(Avaliacao().registrar_nota(5, 'Otimo'))
    media = emp_c._media_avaliacao(emp_v)
    assert media == 4.5

def test_consulta_e_comparacao():
    emp1 = EmpresaMarisqueira('Marisqueira A', '111')
    emp2 = EmpresaMarisqueira('Marisqueira B', '222')
    p1 = Produto()
    p1.cadastrar_produto('Camarão fresco', 'fresco', 60.0, 80, emp1)
    emp1.cadastrar_produto(p1)
    p2 = Produto()
    p2.cadastrar_produto('Siri congelado', 'congelado', 30.0, 120, emp2)
    emp2.cadastrar_produto(p2)
    buyer = EmpresaCompradora('Comprador', '333')
    # consulta por categoria
    frescos = buyer.consultar_produtos([emp1, emp2], categoria='fresco')
    assert len(frescos) == 1
    assert frescos[0].nome == 'Camarão fresco'
    # consulta por nome
    por_nome = buyer.consultar_produtos([emp1, emp2], nome='Siri')
    assert len(por_nome) == 1
    assert por_nome[0].nome == 'Siri congelado'
    # comparação por preco
    ordenados = buyer.comparar_produtos([p1, p2])
    assert ordenados[0].nome == 'Siri congelado'  # menor preco
    assert ordenados[1].nome == 'Camarão fresco'

if __name__ == '__main__':
    test_produto_cadastro_e_estoque()
    test_pedido_fluxo()
    test_avaliacao()
    test_consulta_e_comparacao()
    print('Todos os testes passaram!')