import sys
sys.path.append(r'C:\Users\garci\OneDrive\Área de Trabalho\Exercícios(POO30_09)')
from Empresa import Empresa
from EmpresaMarisqueira import EmpresaMarisqueira
from EmpresaCompradora import EmpresaCompradora
from Produto import Produto

# Setup
emp_m = EmpresaMarisqueira('Marisqueira Teste', '00.000.000/0001-00')
emp_c = EmpresaCompradora('Comprador Teste', '11.111.111/0001-11')
prod = Produto()
prod.cadastrar_produto('Camarão', 'fresco', 45.0, 100, emp_m)
emp_m.cadastrar_produto(prod)

# Test consultar_produtos with avaliacao_min as int
result = emp_c.consultar_produtos([emp_m], nome=None, categoria='fresco', empresa=None, avaliacao_min=0)
print('Consulta succeeded, found', len(result), 'products')
if result:
    print('First product:', result[0].nome)
# Test with string should now be prevented because we pass int
# but we can test that passing string raises TypeError? Not needed.
print('Test passed')