from apis.correios import Correios

cep_origem = '19046-110'
cep_destino = '25651-153'
peso = '0.3'
valor_declarado = '1500'


c = Correios(cep_origem, cep_destino, peso, valor_declarado)
print(c.response())
print(c.get_express_delivery_info())
