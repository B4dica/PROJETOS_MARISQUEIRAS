#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface de terminal simples para o projeto Marisqueiras da Ilha.
Permite cadastrar produtos, alterar quantidade, realizar pedidos,
aceitar/rejeitar/solicitar ajuste, atualizar status de entrega,
consultar produtos, comparar, avaliar empresa, verificar disponibilidade,
adicionar item ao pedido, validar quantidade e registrar nota.
"""

import sys
import os

# Garante que o diretório atual esteja no path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Empresa import Empresa
from EmpresaMarisqueira import EmpresaMarisqueira
from EmpresaCompradora import EmpresaCompradora
from Produto import Produto
from Pedido import Pedido
from ItemPedido import ItemPedido
from Avaliacao import Avaliacao


def linha():
    print("-" * 50)


def menu_principal():
    print("\n=== MARISQUEIRAS DA ILHA - SISTEMA TERMINAL ===")
    print("1 - Cadastrar empresa marisqueira")
    print("2 - Cadastrar empresa compradora")
    print("3 - Cadastrar produto")
    print("4 - Alterar quantidade de produto")
    print("5 - Realizar pedido")
    print("6 - Receber pedido (vista marisqueira)")
    print("7 - Aceitar pedido")
    print("8 - Rejeitar pedido")
    print("9 - Solicitar ajuste no pedido")
    print("10 - Atualizar status de entrega")
    print("11 - Consultar produtos (por filtros)")
    print("12 - Comparar produtos (por preço)")
    print("13 - Avaliar empresa marisqueira")
    print("14 - Verificar disponibilidade de produto")
    print("15 - Adicionar item ao pedido")
    print("16 - Validar quantidade de item")
    print("17 - Registrar nota de avaliação")
    print("0 - Sair")
    linha()


def main():
    # armazenamentos simples em memória
    empresas_marisqueiras = []
    empresas_compradoras = []
    produtos = []
    pedidos = []
    avaliacoes = []

    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "0":
            print("Encerrando...")
            break
        elif escolha == "1":
            # cadastrar empresa marisqueira
            nome = input("Nome da empresa marisqueira: ").strip()
            cnpj = input("CNPJ: ").strip()
            emp = EmpresaMarisqueira(nome, cnpj)
            empresas_marisqueiras.append(emp)
            print(f"Empresa marisqueira '{nome}' cadastrada.")
        elif escolha == "2":
            nome = input("Nome da empresa compradora: ").strip()
            cnpj = input("CNPJ: ").strip()
            emp = EmpresaCompradora(nome, cnpj)
            empresas_compradoras.append(emp)
            print(f"Empresa compradora '{nome}' cadastrada.")
        elif escolha == "3":
            if not empresas_marisqueiras:
                print("Cadastre primeiro uma empresa marisqueira.")
                continue
            nome = input("Nome do produto: ").strip()
            categoria = input("Categoria (fresco/congelado): ").strip().lower()
            while categoria not in ("fresco", "congelado"):
                categoria = input("Categoria inválida. Digite fresco ou congelado: ").strip().lower()
            preco = float(input("Preço por kg: ").strip())
            quantidade = float(input("Quantidade em estoque (kg): ").strip())
            # escolher empresa
            print("Selecione a empresa marisqueira:")
            for i, e in enumerate(empresas_marisqueiras):
                print(f"  {i+1} - {e.nome}")
            idx = int(input("Número: ")) - 1
            empresa = empresas_marisqueiras[idx]
            prod = Produto()
            prod.cadastrar_produto(nome, categoria, preco, quantidade, empresa)
            empresa.cadastrar_produto(prod)
            produtos.append(prod)
            print(f"Produto '{nome}' cadastrado na empresa {empresa.nome}.")
        elif escolha == "4":
            if not produtos:
                print("Nenhum produto cadastrado.")
                continue
            print("Produtos disponíveis:")
            for i, p in enumerate(produtos):
                print(f"  {i+1} - {p.nome} (estoque: {p.quantidade} kg)")
            idx = int(input("Número do produto: ")) - 1
            nova_qtd = float(input("Nova quantidade (kg): "))
            produtos[idx].alterar_quantidade(nova_qtd)
            print(f"Quantidade atualizada para {nova_qtd} kg.")
        elif escolha == "5":
            if not empresas_compradoras or not empresas_marisqueiras:
                print("É necessário ter ao menos uma empresa compradora e uma marisqueira.")
                continue
            print("Selecione a empresa compradora:")
            for i, e in enumerate(empresas_compradoras):
                print(f"  {i+1} - {e.nome}")
            comp_idx = int(input("Número: ")) - 1
            compradora = empresas_compradoras[comp_idx]
            print("Selecione a empresa marisqueira (vendedor):")
            for i, e in enumerate(empresas_marisqueiras):
                print(f"  {i+1} - {e.nome}")
            vend_idx = int(input("Número: ")) - 1
            vendedor = empresas_marisqueiras[vend_idx]
            # lista de produtos do vendedor
            if not vendedor.produtos:
                print("O vendedor não tem produtos cadastrados.")
                continue
            print("Produtos disponíveis do vendedor:")
            for i, p in enumerate(vendedor.produtos):
                print(f"  {i+1} - {p.nome} (R$ {p.preco}/kg, estoque: {p.quantidade} kg)")
            escolhas = input("Digite os números dos produtos separados por vírgula (ex: 1,3): ").strip()
            prod_qtde = {}
            for num in escolhas.split(","):
                num = num.strip()
                if not num:
                    continue
                p_idx = int(num) - 1
                produto = vendedor.produtos[p_idx]
                qtd = float(input(f"Quantidade (kg) para {produto.nome}: "))
                prod_qtde[produto] = qtd
            endereco = input("Endereço de entrega: ").strip()
            tempo = input("Tempo de entrega (ex: 2 dias): ").strip()
            try:
                pedido = compradora.realizar_pedido(vendedor, prod_qtde, endereco, tempo)
                pedidos.append(pedido)
                print(f"Pedido realizado com sucesso! ID temporário: {id(pedido)}")
            except ValueError as e:
                print(f"Erro ao realizar pedido: {e}")
        elif escolha == "6":
            if not pedidos:
                print("Nenhum pedido realizado.")
                continue
            print("Pedidos pendentes (status Recebido):")
            pendentes = [p for p in pedidos if p.status == "Recebido"]
            if not pendentes:
                print("Nenhum pedido pendente.")
                continue
            for i, p in enumerate(pendentes):
                print(f"  {i+1} - Pedido de {p.comprador.nome} para {p.vendedor.nome}")
            idx = int(input("Número do pedido a receber: ")) - 1
            pedido = pendentes[idx]
            # o vendedor já foi notificado no realizar_pedido, mas podemos chamar novamente
            msg = vendedor.receber_pedido(pedido) if hasattr(vendedor, 'receber_pedido') else "Pedido já recebido."
            print(msg)
        elif escolha == "7":
            if not pedidos:
                print("Nenhum pedido.")
                continue
            print("Pedidos aguardando decisão:")
            pendentes = [p for p in pedidos if p.status in ("Recebido", "Aceito", "Rejeitado", "Ajuste Solicitado")]
            for i, p in enumerate(pendentes):
                print(f"  {i+1} - {p.status} - {p.comprador.nome} -> {p.vendedor.nome}")
            idx = int(input("Número do pedido: ")) - 1
            pedido = pendentes[idx]
            # precisamos saber quem é o vendedor
            vendedor = pedido.vendedor
            msg = vendedor.aceitar_pedido(pedido)
            print(msg)
        elif escolha == "8":
            if not pedidos:
                print("Nenhum pedido.")
                continue
            print("Pedidos aguardando decisão:")
            pendentes = [p for p in pedidos if p.status in ("Recebido", "Aceito", "Rejeitado", "Ajuste Solicitado")]
            for i, p in enumerate(pendentes):
                print(f"  {i+1} - {p.status} - {p.comprador.nome} -> {p.vendedor.nome}")
            idx = int(input("Número do pedido: ")) - 1
            pedido = pendentes[idx]
            vendedor = pedido.vendedor
            motivo = input("Motivo da rejeição: ").strip()
            msg = vendedor.rejeitar_pedido(pedido, motivo)
            print(msg)
        elif escolha == "9":
            if not pedidos:
                print("Nenhum pedido.")
                continue
            print("Pedidos aguardando decisão:")
            pendentes = [p for p in pedidos if p.status in ("Recebido", "Aceito", "Rejeitado", "Ajuste Solicitado")]
            for i, p in enumerate(pendentes):
                print(f"  {i+1} - {p.status} - {p.comprador.nome} -> {p.vendedor.nome}")
            idx = int(input("Número do pedido: ")) - 1
            pedido = pendentes[idx]
            vendedor = pedido.vendedor
            ajustes = input("Descreva o ajuste solicitado: ").strip()
            msg = vendedor.solicitar_ajuste(pedido, ajustes)
            print(msg)
        elif escolha == "10":
            if not pedidos:
                print("Nenhum pedido.")
                continue
            print("Pedidos:")
            for i, p in enumerate(pedidos):
                print(f"  {i+1} - {p.status} - Entrega: {p.status_entrega}")
            idx = int(input("Número do pedido: ")) - 1
            pedido = pedidos[idx]
            vendedor = pedido.vendedor
            novo_status = input("Novo status de entrega (Pendente, Em Transporte, Entregue): ").strip()
            msg = vendedor.atualizar_status_entrega(pedido, novo_status)
            print(msg)
        elif escolha == "11":
            if not empresas_marisqueiras:
                print("Nenhuma empresa marisqueira cadastrada.")
                continue
            print("Selecione as empresas para consulta (deixe vazio para todas):")
            for i, e in enumerate(empresas_marisqueiras):
                print(f"  {i+1} - {e.nome}")
            selec = input("Números separados por vírgula (ou Enter para todas): ").strip()
            if selec == "":
                vendedores = empresas_marisqueiras
            else:
                indices = [int(x)-1 for x in selec.split(",") if x.strip()]
                vendedores = [empresas_marisqueiras[i] for i in indices]
            nome_f = input("Filtrar por nome (deixe vazio para ignorar): ").strip() or None
            cat_f = input("Filtrar por categoria (fresco/congelado, vazio ignora): ").strip().lower()
            if cat_f not in ("fresco", "congelado"):
                cat_f = None
            emp_f = input("Filtrar por nome da empresa (vazio ignora): ").strip() or None
            aval_f = input("Avaliação mínima em estrelas (0-5, vazio ignora): ").strip()
            aval_min = float(aval_f) if aval_f else 0
            # precisamos de uma compradora para usar o método consultar_produtos
            if not empresas_compradoras:
                print("Cadastre uma empresa compradora para usar a consulta.")
                continue
            compradora = empresas_compradoras[0]
            resultados = compradora.consultar_produtos(vendedores, nome=nome_f, categoria=cat_f,
                                                       empresa=emp_f, avaliacao_min=aval_min)
            print("\nResultado da consulta:")
            if not resultados:
                print("Nenhum produto encontrado.")
            else:
                for p in resultados:
                    print(f"- {p.nome} ({p.categoria}) - R$ {p.preco}/kg - Estoque: {p.quantidade} kg - Empresa: {p.empresa.nome}")
        elif escolha == "12":
            if not produtos:
                print("Nenhum produto cadastrado.")
                continue
            print("Produtos disponíveis para comparação:")
            for i, p in enumerate(produtos):
                print(f"  {i+1} - {p.nome} - R$ {p.preco}/kg - {p.empresa.nome}")
            selec = input("Digite os números dos produtos a comparar (vírgula): ").strip()
            indices = [int(x)-1 for x in selec.split(",") if x.strip()]
            lista = [produtos[i] for i in indices]
            if not empresas_compradoras:
                print("Cadastre uma empresa compradora.")
                continue
            compradora = empresas_compradoras[0]
            ordenados = compradora.comparar_produtos(lista)
            print("\nProdutos ordenados por preço (menor → maior):")
            for p in ordenados:
                print(f"- {p.nome}: R$ {p.preco}/kg ({p.empresa.nome})")
        elif escolha == "13":
            if not empresas_compradoras or not empresas_marisqueiras:
                print("É necessário ter ao menos uma compradora e uma marisqueira.")
                continue
            print("Selecione a empresa compradora (avaliadora):")
            for i, e in enumerate(empresas_compradoras):
                print(f"  {i+1} - {e.nome}")
            comp_idx = int(input("Número: ")) - 1
            compradora = empresas_compradoras[comp_idx]
            print("Selecione a empresa marisqueira a ser avaliada:")
            for i, e in enumerate(empresas_marisqueiras):
                print(f"  {i+1} - {e.nome}")
            vend_idx = int(input("Número: ")) - 1
            vendedor = empresas_marisqueiras[vend_idx]
            nota = float(input("Nota (1 a 5): ").strip())
            comentario = input("Comentário (opcional): ").strip()
            avaliacao = compradora.avaliar_empresa(vendedor, nota, comentario)
            avaliacoes.append(avaliacao)
            print(f"Avaliação registrada: {avaliacao.nota} estrelas.")
        elif escolha == "14":
            if not produtos:
                print("Nenhum produto.")
                continue
            print("Produtos:")
            for i, p in enumerate(produtos):
                print(f"  {i+1} - {p.nome} - Estoque: {p.quantidade} kg")
            idx = int(input("Número do produto: ")) - 1
            produto = produtos[idx]
            qtd = float(input("Quantidade desejada (kg): ").strip())
            if not empresas_compradoras:
                print("Cadastre uma empresa compradora.")
                continue
            compradora = empresas_compradoras[0]
            disp = compradora.verificar_disponibilidade(produto, qtd)
            print(f"Disponível? {'Sim' if disp else 'Não'} (estoque {produto.quantidade} kg)")
        elif escolha == "15":
            if not pedidos:
                print("Nenhum pedido.")
                continue
            print("Pedidos:")
            for i, p in enumerate(pedidos):
                print(f"  {i+1} - {p.status}")
            idx = int(input("Número do pedido: ")) - 1
            pedido = pedidos[idx]
            if not produtos:
                print("Nenhum produto cadastrado.")
                continue
            print("Produtos:")
            for i, p in enumerate(produtos):
                print(f"  {i+1} - {p.nome} - Estoque: {p.quantidade} kg")
            p_idx = int(input("Número do produto: ")) - 1
            produto = produtos[p_idx]
            qtd = float(input("Quantidade (kg): ").strip())
            item = pedido.adicionar_item(produto, qtd)
            print(f"Item adicionado: {produto.nome} - {qtd} kg")
        elif escolha == "16":
            if not pedidos:
                print("Nenhum pedido.")
                continue
            print("Pedidos com items:")
            pedidos_com_itens = [p for p in pedidos if p.itens]
            if not pedidos_com_itens:
                print("Nenhum pedido tem items.")
                continue
            for i, p in enumerate(pedidos_com_itens):
                print(f"  {i+1} - Pedido {id(p)} - {len(p.itens)} item(ns)")
            idx = int(input("Número do pedido: ")) - 1
            pedido = pedidos_com_itens[idx]
            if not pedido.itens:
                print("Pedido sem items.")
                continue
            print("Items do pedido:")
            for i, item in enumerate(pedido.itens):
                print(f"  {i+1} - {item.produto.nome} - {item.quantidade} kg")
            i_idx = int(input("Número do item: ")) - 1
            item = pedido.itens[i_idx]
            valido, msg = item.validar_quantidade()
            print(f"Validação: {'Válido' if valido else 'Inválido'} - {msg}")
        elif escolha == "17":
            if not avaliacoes:
                print("Nenhuma avaliação registrada.")
                continue
            print("Avaliações:")
            for i, a in enumerate(avaliacoes):
                print(f"  {i+1} - {a.nota} estrelas - {a.comentario} - Empresa: {a.empresa_avaliada.nome}")
            idx = int(input("Número da avaliação: ")) - 1
            avaliacao = avaliacoes[idx]
            nota = avaliacao.avaliar_empresa()
            print(f"Nota da avaliação: {nota}")
        else:
            print("Opção inválida. Tente novamente.")
        linha()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        sys.exit(0)