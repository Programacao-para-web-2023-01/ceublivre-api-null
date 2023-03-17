import requests
from xml.etree import ElementTree

cep_origem = '19046-110'
cep_destino = '25651-153'
peso = '0.3'
valor_declarado = '1500'

url_api = f'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?nCdEmpresa=&sDsSenha=&nCdServico=41106&sCepOrigem={cep_origem}&sCepDestino={cep_destino}&nVlPeso={peso}&nCdFormato=1&nVlComprimento=20&nVlAltura=10&nVlLargura=15&nVlValorDeclarado={valor_declarado}&sCdMaoPropria=n&nVlDiametro=0&sCdAvisoRecebimento=n&StrRetorno=xml&nIndicaCalculo=3'

response = requests.get(url_api, headers={'Content-Type': 'application/xml'})

root = ElementTree.fromstring(response.content)
valor_frete = root.find('.//Valor').text

print(f'O valor do frete é R$ {valor_frete}.')
