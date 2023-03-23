# CeubLivre-API

## Gerenciamento de frete

Este microsserviço gerencia o processo de cálculo e cobrança de frete para os produtos comprados no marketplace,
permitindo que os usuários escolham entre diferentes opções de envio e rastreiem o status de entrega de seus produtos.

### Cálculo de frete (3 pontos)

Calcular o custo do frete com base nas informações de entrega do cliente, peso e dimensões dos produtos e opções de
frete disponíveis.

### Seleção de frete (2 pontos)

Fornecer ao cliente opções de frete disponíveis com base em sua localização e tempo de entrega, permitindo que eles
selecionem a melhor opção para suas necessidades.

### Integração de transportadoras (3 pontos por transportadora)

Integrar-se com as transportadoras para realizar cálculos precisos de frete e obter informações de rastreamento
atualizadas.

### Rastreamento de frete (3 pontos)

Permitir que os clientes rastreiem o status de seus pedidos, fornecendo informações atualizadas sobre o envio e entrega
dos produtos.

### Relatórios de frete (2 pontos)

Manter um registro detalhado de todos os custos de frete, incluindo informações sobre transportadoras, custos de envio,
prazo de entrega, entre outros. Permitir que os administradores gerem relatórios com base nessas informações.

### Gerenciamento de problemas de entrega (1 ponto)

Gerenciar problemas de entrega, como atrasos ou extravios de encomendas, garantindo que o cliente receba o produto ou
seja reembolsado adequadamente.

**Total: pelo menos 14 pontos**

---

# Setup

```bash
# Create a virtual environment
python -m venv venv

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```
