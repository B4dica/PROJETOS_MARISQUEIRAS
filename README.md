<mxfile host="app.diagrams.net">
  <diagram name="Página-1" id="578jPa3SbGRa3Ajrvy4l">
    <mxGraphModel dx="3948" dy="1606" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <UserObject label="" plantUmlData="{&#xa;  &quot;data&quot;: &quot;@startuml\nskinparam classAttributeIconSize 0\nskinparam linetype ortho\nskinparam nodesep 60\nskinparam ranksep 60\nskinparam shadowing false\nskinparam class {\n  BackgroundColor #FEFEFE\n  BorderColor #333333\n  ArrowColor #333333\n  HeaderBackgroundColor #E8F1FB\n}\nskinparam note {\n  BackgroundColor #FFF8DC\n  BorderColor #B8860B\n}\n\ntitle **Marisqueiras da Ilha — Diagrama de Classes**\n\n&#39; ============================================\n&#39; CLASSES PRINCIPAIS\n&#39; ============================================\n\nclass \&quot;EMPRESA_MARISQUEIRA\&quot; as EmpresaMarisqueira {\n  - id_empresa_marisqueira : CNPJ\n  - nome : String\n  - localizacao : Localizacao\n}\n\nclass \&quot;EMPRESA_COMPRADORA\&quot; as EmpresaCompradora {\n  - id_empresa_compradora : CNPJ\n  - nome : String\n  - localizacao : Localizacao\n}\n\nclass \&quot;PRODUTO\&quot; as Produto {\n  - id_produto : int\n  - nome : String\n  - categoria : CategoriaProduto\n  - preco : Decimal\n  - quantidade_disponivel : Decimal\n  - fotografia : Image [0..1]\n  + estaDisponivel() : boolean\n}\n\nclass \&quot;PEDIDO\&quot; as Pedido {\n  - id_pedido : int\n  - endereco_entrega : Endereco\n  - tempo_entrega : Time\n  - status_pedido : StatusPedido\n  + adicionarItem(produto, qtd) : void\n  + finalizar() : void\n}\n\nclass \&quot;ITEM_PEDIDO\&quot; as ItemPedido {\n  - id_pedido : int\n  - id_produto : int\n  - quantidade : Decimal\n  + validarQuantidade() : boolean\n}\n\nclass \&quot;AVALIACAO\&quot; as Avaliacao {\n  - id_avaliacao : int\n  - nota : int\n  + validarNota() : boolean\n}\n\n&#39; ============================================\n&#39; ENUMERAÇÕES\n&#39; ============================================\n\nenum \&quot;CategoriaProduto\&quot; as CategoriaProduto {\n  FRESCO\n  CONGELADO\n}\n\nenum \&quot;StatusPedido\&quot; as StatusPedido {\n  EM_PREPARO\n  EM_CURSO\n  FINALIZADO\n}\n\n&#39; ============================================\n&#39; RELACIONAMENTOS\n&#39; ============================================\n\n&#39; Empresa Marisqueira fornece produtos\nEmpresaMarisqueira \&quot;1\&quot; -- \&quot;0..*\&quot; Produto : fornece &gt;\n\n&#39; Empresa Compradora realiza pedidos\nEmpresaCompradora \&quot;1\&quot; -- \&quot;0..*\&quot; Pedido : realiza &gt;\n\n&#39; Empresa Marisqueira entrega pedidos\nEmpresaMarisqueira \&quot;1\&quot; -- \&quot;0..*\&quot; Pedido : entrega &gt;\n\n&#39; Pedido contém itens\nPedido \&quot;1\&quot; *-- \&quot;1..*\&quot; ItemPedido : contém &gt;\n\n&#39; Produto participa de itens\nProduto \&quot;1\&quot; -- \&quot;0..*\&quot; ItemPedido : participa &gt;\n\n&#39; Pedido pode ter avaliações\nPedido \&quot;1\&quot; -- \&quot;0..*\&quot; Avaliacao : recebe &gt;\n\n&#39; Produto usa categoria\nProduto --&gt; CategoriaProduto\n\n&#39; Pedido usa status\nPedido --&gt; StatusPedido\n\n&#39; ============================================\n&#39; NOTAS DE RESTRIÇÕES\n&#39; ============================================\n\nnote right of Produto\n  • categoria: FRESCO ou CONGELADO\n  • frescos e congelados = produtos distintos\n  • quantidade_disponivel em kg\n  • qtd = 0 → permanece cadastrado\n    como **indisponível**\n  • fotografia é opcional\nend note\n\nnote bottom of ItemPedido\n  • quantidade mínima: **25 kg**\n  • quantidade ≤ disponibilidade do produto\n  • entidade associativa\n    PEDIDO × PRODUTO\nend note\n\nnote bottom of Pedido\n  • todos os produtos do pedido devem\n    pertencer à **mesma EMPRESA_MARISQUEIRA**\n  • sem valor financeiro mínimo\n  • entrega feita pela própria marisqueira\n    (sem rastreamento em tempo real)\n  • pagamento fora do escopo\nend note\n\nnote right of Avaliacao\n  • nota entre 1 e 5 estrelas\n  • cardinalidade não definida\n    pelo requisito\nend note\n\nnote top of EmpresaMarisqueira\n  • responsável pelo fornecimento\n    dos produtos e pela entrega\nend note\n\nnote top of EmpresaCompradora\n  • especialização de EMPRESA\n  • realiza as compras\nend note\n\n@enduml&quot;,&#xa;  &quot;config&quot;: null&#xa;}" id="HGRX3kLrjE_t7XVL2oVv-1">
          <mxCell connectable="0" parent="1" style="group;transparentBounds=1;editIcon=1;lockedGroup=0;groupPadding=10;" vertex="1">
            <mxGeometry as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="Marisqueiras da Ilha — Diagrama de Classes" plantUmlId="cltitle_2" plantUmlBaseStyle="text;html=1;fillColor=none;strokeColor=none;fontSize=14;fontStyle=1;fontColor=#000000;align=center;verticalAlign=middle;" plantUmlBaseValue="Marisqueiras da Ilha — Diagrama de Classes" id="HGRX3kLrjE_t7XVL2oVv-2">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="text;html=1;fillColor=none;strokeColor=none;fontSize=14;fontStyle=1;fontColor=#000000;align=center;verticalAlign=middle;" vertex="1">
            <mxGeometry height="24" width="341.69660000000005" x="372.14669999999995" y="226" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="EMPRESA_MARISQUEIRA" plantUmlId="cls_3" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="EMPRESA_MARISQUEIRA" id="HGRX3kLrjE_t7XVL2oVv-3">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="93.46999999999998" width="246.23" x="269.99999999999994" y="380.62" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_empresa_marisqueira : CNPJ" plantUmlId="mb_5" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_empresa_marisqueira : CNPJ" id="HGRX3kLrjE_t7XVL2oVv-5">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-3" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_6" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-6">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-5" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="nome : String" plantUmlId="mb_7" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="nome : String" id="HGRX3kLrjE_t7XVL2oVv-7">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-3" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_8" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-8">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-7" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="localizacao : Localizacao" plantUmlId="mb_9" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="localizacao : Localizacao" id="HGRX3kLrjE_t7XVL2oVv-9">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-3" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_10" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-10">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-9" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_11" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-11">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-3" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="246.23" y="85.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="EMPRESA_COMPRADORA" plantUmlId="cls_12" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="EMPRESA_COMPRADORA" id="HGRX3kLrjE_t7XVL2oVv-12">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="93.46999999999998" width="238.33" x="640.0049999999999" y="380.62" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_empresa_compradora : CNPJ" plantUmlId="mb_14" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_empresa_compradora : CNPJ" id="HGRX3kLrjE_t7XVL2oVv-14">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-12" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="238.33" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_15" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-15">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-14" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="nome : String" plantUmlId="mb_16" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="nome : String" id="HGRX3kLrjE_t7XVL2oVv-16">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-12" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="238.33" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_17" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-17">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-16" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="localizacao : Localizacao" plantUmlId="mb_18" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="localizacao : Localizacao" id="HGRX3kLrjE_t7XVL2oVv-18">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-12" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="238.33" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_19" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-19">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-18" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_20" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-20">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-12" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="238.33" y="85.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="PRODUTO" plantUmlId="cls_21" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="PRODUTO" id="HGRX3kLrjE_t7XVL2oVv-21">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="159.42999999999998" width="246.23" x="259.995" y="555.9999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_produto : int" plantUmlId="mb_23" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_produto : int" id="HGRX3kLrjE_t7XVL2oVv-23">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_24" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-24">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-23" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="nome : String" plantUmlId="mb_25" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="nome : String" id="HGRX3kLrjE_t7XVL2oVv-25">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_26" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-26">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-25" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="categoria : CategoriaProduto" plantUmlId="mb_27" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="categoria : CategoriaProduto" id="HGRX3kLrjE_t7XVL2oVv-27">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_28" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-28">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-27" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="preco : Decimal" plantUmlId="mb_29" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="preco : Decimal" id="HGRX3kLrjE_t7XVL2oVv-29">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="85.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_30" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-30">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-29" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="quantidade_disponivel : Decimal" plantUmlId="mb_31" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="quantidade_disponivel : Decimal" id="HGRX3kLrjE_t7XVL2oVv-31">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="101.95999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_32" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-32">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-31" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="fotografia : Image [0..1]" plantUmlId="mb_33" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="fotografia : Image [0..1]" id="HGRX3kLrjE_t7XVL2oVv-33">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="118.44999999999997" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_34" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-34">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-33" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_35" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-35">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="246.23" y="134.93999999999997" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="estaDisponivel() : boolean" plantUmlId="mb_36" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="estaDisponivel() : boolean" id="HGRX3kLrjE_t7XVL2oVv-36">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-21" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="246.23" y="142.93999999999997" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_37" plantUmlBaseStyle="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-37">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-36" style="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="PEDIDO" plantUmlId="cls_38" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="PEDIDO" id="HGRX3kLrjE_t7XVL2oVv-38">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="126.44999999999997" width="307.9999999999999" x="611.485" y="555.995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_pedido : int" plantUmlId="mb_40" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_pedido : int" id="HGRX3kLrjE_t7XVL2oVv-40">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-38" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="307.9999999999999" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_41" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-41">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-40" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="endereco_entrega : Endereco" plantUmlId="mb_42" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="endereco_entrega : Endereco" id="HGRX3kLrjE_t7XVL2oVv-42">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-38" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="307.9999999999999" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_43" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-43">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-42" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="status_pedido : StatusPedido" plantUmlId="mb_46" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="status_pedido : StatusPedido" id="HGRX3kLrjE_t7XVL2oVv-46">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-38" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="307.9999999999999" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_47" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-47">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-46" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_48" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-48">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-38" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="307.9999999999999" y="85.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="adicionarItem(produto, qtd) : void" plantUmlId="mb_49" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="adicionarItem(produto, qtd) : void" id="HGRX3kLrjE_t7XVL2oVv-49">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-38" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="307.9999999999999" y="93.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_50" plantUmlBaseStyle="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-50">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-49" style="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="finalizar() : void" plantUmlId="mb_51" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="finalizar() : void" id="HGRX3kLrjE_t7XVL2oVv-51">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-38" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="307.9999999999999" y="109.95999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_52" plantUmlBaseStyle="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-52">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-51" style="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="ITEM_PEDIDO" plantUmlId="cls_53" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="ITEM_PEDIDO" id="HGRX3kLrjE_t7XVL2oVv-53">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="109.95999999999998" width="226.44" x="454.2600000000001" y="838.24" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_pedido : int" plantUmlId="mb_55" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_pedido : int" id="HGRX3kLrjE_t7XVL2oVv-55">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-53" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="226.44" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_56" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-56">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-55" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_produto : int" plantUmlId="mb_57" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_produto : int" id="HGRX3kLrjE_t7XVL2oVv-57">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-53" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="226.44" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_58" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-58">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-57" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="quantidade : Decimal" plantUmlId="mb_59" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="quantidade : Decimal" id="HGRX3kLrjE_t7XVL2oVv-59">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-53" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="226.44" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_60" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-60">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-59" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_61" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-61">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-53" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="226.44" y="85.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="validarQuantidade() : boolean" plantUmlId="mb_62" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="validarQuantidade() : boolean" id="HGRX3kLrjE_t7XVL2oVv-62">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-53" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="226.44" y="93.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_63" plantUmlBaseStyle="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-63">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-62" style="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="AVALIACAO" plantUmlId="cls_64" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="AVALIACAO" id="HGRX3kLrjE_t7XVL2oVv-64">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="93.46999999999998" width="179.92" x="820" y="856.985" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="id_avaliacao : int" plantUmlId="mb_66" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="id_avaliacao : int" id="HGRX3kLrjE_t7XVL2oVv-66">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-64" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="179.92" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_67" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-67">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-66" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="nota : int" plantUmlId="mb_68" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="nota : int" id="HGRX3kLrjE_t7XVL2oVv-68">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-64" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="179.92" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_69" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-69">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-68" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_70" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-70">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-64" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="179.92" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="validarNota() : boolean" plantUmlId="mb_71" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="validarNota() : boolean" id="HGRX3kLrjE_t7XVL2oVv-71">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-64" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="179.92" y="76.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_72" plantUmlBaseStyle="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-72">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-71" style="ellipse;fillColor=#84BE84;strokeColor=#038048;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="CategoriaProduto" plantUmlId="cls_73" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="CategoriaProduto" id="HGRX3kLrjE_t7XVL2oVv-73">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="76.97999999999999" width="150.69" x="259.99" y="780" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="FRESCO" plantUmlId="mb_75" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="FRESCO" id="HGRX3kLrjE_t7XVL2oVv-75">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-73" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="150.69" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="CONGELADO" plantUmlId="mb_76" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="CONGELADO" id="HGRX3kLrjE_t7XVL2oVv-76">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-73" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="150.69" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_77" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-77">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-73" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="150.69" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="StatusPedido" plantUmlId="cls_78" plantUmlBaseStyle="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" plantUmlBaseValue="StatusPedido" id="HGRX3kLrjE_t7XVL2oVv-78">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="swimlane;collapsible=0;fontStyle=0;align=center;fontSize=14;fontColor=#000000;startSize=32;spacingLeft=25;fillColor=#E8F1FB;strokeColor=#333333;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;marginBottom=0;stackSpacing=0;marginTop=4;shadow=0;swimlaneFillColor=#FEFEFE;" vertex="1">
            <mxGeometry height="93.46999999999998" width="119.38" x="717.2799999999997" y="740.005" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="EM_PREPARO" plantUmlId="mb_80" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="EM_PREPARO" id="HGRX3kLrjE_t7XVL2oVv-80">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-78" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="119.38" y="36" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="EM_CURSO" plantUmlId="mb_81" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="EM_CURSO" id="HGRX3kLrjE_t7XVL2oVv-81">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-78" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="119.38" y="52.489999999999995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="FINALIZADO" plantUmlId="mb_82" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="FINALIZADO" id="HGRX3kLrjE_t7XVL2oVv-82">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-78" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="16.49" width="119.38" y="68.97999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="clssep_83" plantUmlBaseStyle="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-83">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-78" style="line;strokeWidth=0.5;strokeColor=#333333;fillColor=none;align=left;verticalAlign=middle;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;connectable=0;" vertex="1">
            <mxGeometry height="8" width="119.38" y="85.46999999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="fornece &amp;gt;" plantUmlId="rel_84" plantUmlBaseStyle="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.463;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="fornece &amp;gt;" id="HGRX3kLrjE_t7XVL2oVv-84">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-3" style="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.463;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" target="HGRX3kLrjE_t7XVL2oVv-21">
            <mxGeometry relative="1" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="1" plantUmlId="qty_85" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1" id="HGRX3kLrjE_t7XVL2oVv-85">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-84" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="13" x="-1" as="geometry">
              <mxPoint x="-13" y="7.89" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="0..*" plantUmlId="qty_86" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="0..*" id="HGRX3kLrjE_t7XVL2oVv-86">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-84" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="27" x="1" as="geometry">
              <mxPoint x="-27" y="-23.5" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="realiza &amp;gt;" plantUmlId="rel_87" plantUmlBaseStyle="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.52;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="realiza &amp;gt;" id="HGRX3kLrjE_t7XVL2oVv-87">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-12" style="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.52;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" target="HGRX3kLrjE_t7XVL2oVv-38">
            <mxGeometry relative="1" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="1" plantUmlId="qty_88" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1" id="HGRX3kLrjE_t7XVL2oVv-88">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-87" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="13" x="-1" as="geometry">
              <mxPoint x="-13" y="7.89" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="0..*" plantUmlId="qty_89" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="0..*" id="HGRX3kLrjE_t7XVL2oVv-89">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-87" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="27" x="1" as="geometry">
              <mxPoint x="-27" y="-23.25" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="entrega &amp;gt;" plantUmlId="rel_90" plantUmlBaseStyle="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;verticalAlign=bottom;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="entrega &amp;gt;" id="HGRX3kLrjE_t7XVL2oVv-90">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" style="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;verticalAlign=bottom;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;entryX=0.093;entryY=-0.006;entryDx=0;entryDy=0;entryPerimeter=0;">
            <mxGeometry relative="1" x="0.1012" as="geometry">
              <Array as="points">
                <mxPoint x="507.42" y="520.76" />
                <mxPoint x="627.42" y="520.76" />
              </Array>
              <mxPoint x="507.42" y="470.76" as="sourcePoint" />
              <mxPoint x="627.5489999999999" y="555.9962999999998" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="1" plantUmlId="qty_91" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1" id="HGRX3kLrjE_t7XVL2oVv-91">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-90" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="13" x="-1" as="geometry">
              <mxPoint x="-13" y="7.89" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="0..*" plantUmlId="qty_92" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="0..*" id="HGRX3kLrjE_t7XVL2oVv-92">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-90" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="27" x="1" as="geometry">
              <mxPoint x="-27.38" y="-23.79" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="contém &amp;gt;" plantUmlId="rel_93" plantUmlBaseStyle="startArrow=diamond;startFill=1;startSize=12;endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;verticalAlign=bottom;curved=0;rounded=0;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="contém &amp;gt;" id="HGRX3kLrjE_t7XVL2oVv-93">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-51" style="startArrow=none;startFill=0;startSize=12;endArrow=none;html=1;strokeColor=default;fontColor=#000000;fontSize=13;verticalAlign=bottom;curved=0;rounded=0;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;fixedPointSpacing=1;jumpStyle=none;exitX=0.224;exitY=1.074;exitDx=0;exitDy=0;exitPerimeter=0;endFill=0;">
            <mxGeometry relative="1" x="0.412" y="10" as="geometry">
              <mxPoint as="offset" />
              <Array as="points">
                <mxPoint x="680" y="760" />
                <mxPoint x="620" y="760" />
              </Array>
              <mxPoint x="620" y="830" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="1" plantUmlId="qty_94" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1" id="HGRX3kLrjE_t7XVL2oVv-94">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-93" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="13" x="-1" as="geometry">
              <mxPoint x="-19" y="-18.15" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="1..*" plantUmlId="qty_95" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1..*" id="HGRX3kLrjE_t7XVL2oVv-95">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-93" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="27" x="0.9936" as="geometry">
              <mxPoint x="-26.94" y="-23.53" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="participa &amp;gt;" plantUmlId="rel_96" plantUmlBaseStyle="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.05;exitY=1;exitDx=0;exitDy=0;entryX=0.594;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="participa &amp;gt;" id="HGRX3kLrjE_t7XVL2oVv-96">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-36" style="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.849;exitY=1.348;exitDx=0;exitDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;exitPerimeter=0;">
            <mxGeometry relative="1" x="0.0483" as="geometry">
              <Array as="points">
                <mxPoint x="469.04" y="760" />
                <mxPoint x="530" y="760" />
              </Array>
              <mxPoint x="530" y="830" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="1" plantUmlId="qty_97" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1" id="HGRX3kLrjE_t7XVL2oVv-97">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-96" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="13" x="-1" as="geometry">
              <mxPoint x="-13" y="7.89" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="0..*" plantUmlId="qty_98" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="0..*" id="HGRX3kLrjE_t7XVL2oVv-98">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-96" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="27" x="0.9897" as="geometry">
              <mxPoint x="-27" y="-23.5" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="recebe &amp;gt;" plantUmlId="rel_99" plantUmlBaseStyle="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.05;exitY=1;exitDx=0;exitDy=0;entryX=0.86;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="recebe &amp;gt;" id="HGRX3kLrjE_t7XVL2oVv-99">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-51" style="endArrow=none;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;exitX=0.96;exitY=1.257;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;labelPosition=right;align=left;curved=0;rounded=0;endSize=6;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;exitPerimeter=0;" target="HGRX3kLrjE_t7XVL2oVv-64">
            <mxGeometry relative="1" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="1" plantUmlId="qty_100" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="1" id="HGRX3kLrjE_t7XVL2oVv-100">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-99" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="13" x="-1" as="geometry">
              <mxPoint x="-13" y="7.89" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="0..*" plantUmlId="qty_101" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" plantUmlBaseValue="0..*" id="HGRX3kLrjE_t7XVL2oVv-101">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-99" style="text;html=1;align=left;verticalAlign=middle;resizable=0;points=[];fillColor=none;strokeColor=none;connectable=0;fontSize=13;fontColor=#000000;" vertex="1">
            <mxGeometry height="16" relative="1" width="27" x="0.9955" as="geometry">
              <mxPoint x="-27" y="-23.01" as="offset" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="rel_102" plantUmlBaseStyle="endArrow=classic;endFill=1;endSize=8;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;curved=0;rounded=0;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-102">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-36" style="endArrow=classic;endFill=1;endSize=8;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;curved=0;rounded=0;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;exitX=0.31;exitY=1.003;exitDx=0;exitDy=0;exitPerimeter=0;" target="HGRX3kLrjE_t7XVL2oVv-73">
            <mxGeometry relative="1" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="rel_103" plantUmlBaseStyle="endArrow=classic;endFill=1;endSize=8;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;curved=0;rounded=0;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-103">
          <mxCell edge="1" parent="HGRX3kLrjE_t7XVL2oVv-1" source="HGRX3kLrjE_t7XVL2oVv-51" style="endArrow=classic;endFill=1;endSize=8;html=1;strokeColor=#333333;fontColor=#000000;fontSize=13;curved=0;rounded=0;sourcePerimeterSpacing=0;targetPerimeterSpacing=0;exitX=0.53;exitY=1.105;exitDx=0;exitDy=0;exitPerimeter=0;" target="HGRX3kLrjE_t7XVL2oVv-78">
            <mxGeometry relative="1" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="  • quantidade mínima: &lt;b&gt;25 kg&lt;/b&gt;&lt;br&gt;  • quantidade ≤ disponibilidade do produto&lt;br&gt;  • entidade associativa&lt;br&gt;    PEDIDO × PRODUTO" plantUmlId="note_106" plantUmlBaseStyle="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;html=1;" plantUmlBaseValue="  • quantidade mínima: &lt;b&gt;25 kg&lt;/b&gt;&lt;br&gt;  • quantidade ≤ disponibilidade do produto&lt;br&gt;  • entidade associativa&lt;br&gt;    PEDIDO × PRODUTO" id="HGRX3kLrjE_t7XVL2oVv-106">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;html=1;" vertex="1">
            <mxGeometry height="71.24" width="298" x="750" y="1020" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="noteptr_107" plantUmlBaseStyle="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=north;part=1;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-107">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-106" style="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=north;part=1;" vertex="1">
            <mxGeometry height="41" width="8" x="144.78" y="-39.860000000000014" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="  • todos os produtos do pedido devem&lt;br&gt;    pertencer à &lt;b&gt;mesma EMPRESA_MARISQUEIRA&lt;/b&gt;&lt;br&gt;  • sem valor financeiro mínimo&lt;br&gt;  • entrega feita pela própria marisqueira&lt;br&gt;    (sem rastreamento em tempo real)&lt;br&gt;  • pagamento fora do escopo" plantUmlId="note_108" plantUmlBaseStyle="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;html=1;" plantUmlBaseValue="  • todos os produtos do pedido devem&lt;br&gt;    pertencer à &lt;b&gt;mesma EMPRESA_MARISQUEIRA&lt;/b&gt;&lt;br&gt;  • sem valor financeiro mínimo&lt;br&gt;  • entrega feita pela própria marisqueira&lt;br&gt;    (sem rastreamento em tempo real)&lt;br&gt;  • pagamento fora do escopo" id="HGRX3kLrjE_t7XVL2oVv-108">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;html=1;" vertex="1">
            <mxGeometry height="101.86" width="336" x="399.9999999999999" y="989.995" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="noteptr_109" plantUmlBaseStyle="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=north;part=1;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-109">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-108" style="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=north;part=1;" vertex="1">
            <mxGeometry height="41" width="8" x="163.67000000000007" y="-39.65499999999997" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="  • nota entre 1 e 5 estrelas&#xa;  • cardinalidade não definida&#xa;    pelo requisito" plantUmlId="note_110" plantUmlBaseStyle="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;" plantUmlBaseValue="  • nota entre 1 e 5 estrelas&#xa;  • cardinalidade não definida&#xa;    pelo requisito" id="HGRX3kLrjE_t7XVL2oVv-110">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;" vertex="1">
            <mxGeometry height="55.93" width="207" x="1030" y="865.255" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="noteptr_111" plantUmlBaseStyle="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=west;part=1;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-111">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-110" style="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=west;part=1;" vertex="1">
            <mxGeometry height="8" width="37" x="-36.360000000000014" y="24.08499999999998" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="  • responsável pelo fornecimento&#xa;    dos produtos e pela entrega" plantUmlId="note_112" plantUmlBaseStyle="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;" plantUmlBaseValue="  • responsável pelo fornecimento&#xa;    dos produtos e pela entrega" id="HGRX3kLrjE_t7XVL2oVv-112">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;" vertex="1">
            <mxGeometry height="40.62" width="234" x="302.8299999999999" y="300" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="noteptr_113" plantUmlBaseStyle="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=south;part=1;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-113">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-112" style="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=south;part=1;" vertex="1">
            <mxGeometry height="41" width="8" x="112.95000000000005" y="39.62" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="  • especialização de EMPRESA&#xa;  • realiza as compras" plantUmlId="note_114" plantUmlBaseStyle="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;" plantUmlBaseValue="  • especialização de EMPRESA&#xa;  • realiza as compras" id="HGRX3kLrjE_t7XVL2oVv-114">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;" vertex="1">
            <mxGeometry height="40.62" width="212" x="659.4899999999999" y="300" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="noteptr_115" plantUmlBaseStyle="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=south;part=1;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-115">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-114" style="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=south;part=1;" vertex="1">
            <mxGeometry height="41" width="8" x="102.35000000000002" y="39.62" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="tempo_entrega : Time" plantUmlId="mb_44" plantUmlBaseStyle="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" plantUmlBaseValue="tempo_entrega : Time" id="HGRX3kLrjE_t7XVL2oVv-44">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-1" style="text;html=1;align=left;verticalAlign=middle;spacingLeft=18;spacingRight=4;rotatable=0;fillColor=none;strokeColor=none;fontSize=14;fontColor=#000000;fontStyle=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;" vertex="1">
            <mxGeometry height="48.55" width="307.9999999999999" x="-49.99500000000002" y="820.005" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="vis_45" plantUmlBaseStyle="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-45">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-44" style="rounded=0;fillColor=none;strokeColor=#C82930;strokeWidth=1;movable=0;connectable=0;" vertex="1">
            <mxGeometry height="6" width="6" x="8" y="5.244999999999999" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="  • categoria: FRESCO ou CONGELADO&lt;br&gt;  • frescos e congelados = produtos distintos&lt;br&gt;  • quantidade_disponivel em kg&lt;br&gt;  • qtd = 0 → permanece cadastrado&lt;br&gt;    como &lt;b&gt;indisponível&lt;/b&gt;&lt;br&gt;  • fotografia é opcional" plantUmlId="note_104" plantUmlBaseStyle="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;html=1;" plantUmlBaseValue="  • categoria: FRESCO ou CONGELADO&lt;br&gt;  • frescos e congelados = produtos distintos&lt;br&gt;  • quantidade_disponivel em kg&lt;br&gt;  • qtd = 0 → permanece cadastrado&lt;br&gt;    como &lt;b&gt;indisponível&lt;/b&gt;&lt;br&gt;  • fotografia é opcional" id="HGRX3kLrjE_t7XVL2oVv-104">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-44" style="shape=note;size=10;fillColor=#FFF8DC;strokeColor=#B8860B;fontSize=13;fontColor=#000000;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=4;shadow=0;html=1;" vertex="1">
            <mxGeometry height="101.86" width="269" x="1" y="-53.31" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="" plantUmlId="noteptr_105" plantUmlBaseStyle="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=west;part=1;" plantUmlBaseValue="" id="HGRX3kLrjE_t7XVL2oVv-105">
          <mxCell parent="HGRX3kLrjE_t7XVL2oVv-104" style="shape=triangle;fillColor=#FFF8DC;strokeColor=#B8860B;strokeWidth=0.5;shadow=0;direction=west;part=1;" vertex="1">
            <mxGeometry height="8" width="32.42019543973941" x="-31.837508143322406" y="46.745000000000005" as="geometry" />
          </mxCell>
        </UserObject>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
