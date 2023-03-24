CREATE TABLE tbStatusPedido(
    idStatusPedido INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nomeStatusPedido VARCHAR(255) NOT NULL
);

INSERT INTO tbStatusPedido (nomeStatusPedido) VALUES
    ('aguardando envio'),
    ('em trânsito'),
    ('entregue'),
    ('aguardando retirada');
