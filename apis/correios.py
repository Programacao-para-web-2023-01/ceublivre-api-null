import requests
from xml.etree import ElementTree
from math import ceil

class Correios:
    def __init__(self, cep_origem, cep_destino, peso, valor_declarado):
        self.cep_origem = cep_origem
        self.cep_destino = cep_destino
        self.peso = peso
        self.valor_declarado = valor_declarado

        url_api = f'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?nCdEmpresa=&sDsSenha=&nCdServico=41106&sCepOrigem={cep_origem}&sCepDestino={cep_destino}&nVlPeso={peso}&nCdFormato=1&nVlComprimento=20&nVlAltura=10&nVlLargura=15&nVlValorDeclarado={valor_declarado}&sCdMaoPropria=n&nVlDiametro=0&sCdAvisoRecebimento=n&StrRetorno=xml&nIndicaCalculo=3'
        response = requests.get(url_api, headers={'Content-Type': 'application/xml'})
        root = ElementTree.fromstring(response.content)

        self.error = int(root.find('.//Erro').text)
        if self.error != 0:
            self.msg_error = root.find('.//MsgErro').text
            return

        valor = root.find('.//Valor').text
        self.valor = float(valor.replace(',', '.'))

        prazo_entrega = root.find('.//PrazoEntrega').text
        self.prazo_entrega = int(prazo_entrega)

        entrega_domiciliar = root.find('.//EntregaDomiciliar').text
        self.entrega_domiciliar = True if (entrega_domiciliar == 'S') else False

        entrega_sabado = root.find('.//EntregaSabado').text
        self.entrega_sabado = True if (entrega_sabado == 'S') else False

    def response(self):
        if self.error != 0:
            return {'error': self.error, 'msg_error': self.msg_error}

        return {
            'valor': self.valor,
            'prazo_entrega': self.prazo_entrega,
            'entrega_domiciliar': self.entrega_domiciliar,
            'entrega_sabado': self.entrega_sabado,
            'entrega_expressa': False
        }

    def get_express_delivery_info(self):
        if self.error != 0:
            return {'error': self.error, 'msg_error': self.msg_error}

        return {
            'valor': round(self.valor * 1.5, 2),
            'prazo_entrega': ceil(self.prazo_entrega / 1.5),
            'entrega_domiciliar': self.entrega_domiciliar,
            'entrega_sabado': True,
            'entrega_expressa': True
        }
