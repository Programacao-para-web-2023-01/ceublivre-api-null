CREATE TABLE tbPedido(
    idPedido INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    rastreamentoPedido VARCHAR(36) NOT NULL DEFAULT(uuid()),
    nomePedido VARCHAR(255) NOT NULL,
    cepOrigemPedido VARCHAR(9) NOT NULL,
    cepDestinoPedido VARCHAR(9) NOT NULL,
    pesoPedido DECIMAL(5, 2) NOT NULL,
    valorDeclaradoPedido DECIMAL(6, 2) NOT NULL,
    expressoPedido BOOL NOT NULL,
    valorEnvioPedido DECIMAL(6, 2) NOT NULL,
    prazoEntregaPedido INT NOT NULL,
    temEntregaDomiciliarPedido BOOL NOT NULL,
    temEntregaSabado BOOL NOT NULL,
    statusPedido INT NOT NULL -- Foreign Key not allowed :(
);
