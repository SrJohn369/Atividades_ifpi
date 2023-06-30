/*
COMANDO SELECT
SINTAXE: 
SELECT [ * | EXPRESSÃO] 
FROM TABELA
[WHERE CONDIÇÃO];
*/

CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nome VARCHAR(50),
  idade INT,
  cidade VARCHAR(50)
);

INSERT INTO clientes (id, nome, idade, cidade) VALUES
  (1, 'João da Silva', 32, 'São Paulo'),
  (2, 'Maria Oliveira', 25, 'Rio de Janeiro'),
  (3, 'Carlos Santos', 47, 'Belo Horizonte');

CREATE TABLE pedidos (
  id INT PRIMARY KEY,
  data DATE,
  valor NUMERIC(10,2),
  cliente_id INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO pedidos (id, data, valor, cliente_id) VALUES
  (1, '2021-01-05', 100.00, 1),
  (2, '2021-02-12', 50.00, 2),
  (3, '2021-03-10', 200.00, 1),
  (4, '2021-03-15', 75.00, 3),
  (5, '2021-04-02', 150.00, 2);

--Selecionar todos os dados da tabela "clientes":
SELECT * FROM clientes;

--Selecionar o nome e a idade dos clientes:
SELECT nome, idade FROM clientes;

--Selecionar o nome e a cidade dos clientes que moram em São Paulo:
SELECT nome, cidade FROM clientes WHERE cidade = 'São Paulo';

--Selecionar o valor e a data dos pedidos com valor maior
-- que R$ 100:
SELECT valor, data FROM pedidos WHERE valor > 100;

--Lista de exercícios básicos
    1- Selecione o nome e a idade dos clientes com idade maior
     que 30 anos.
    2- Selecione o nome e o id dos clientes que moram em 
    São Paulo.
    3- Selecione o nome, a idade e a cidade dos clientes que 
    moram em Belo Horizonte.
    4- Selecione o nome, a idade e a cidade dos clientes que 
    moram em Belo Horizonte ou no Rio de Janeiro.
    5- Selecione o nome, a idade e o id dos clientes que 
    moram em São Paulo e têm idade entre 25 e 35 anos.
    6- Selecione o nome e a idade dos clientes que não moram 
    em São Paulo e têm idade maior que 40 anos.
    7- Selecione a data e o valor dos pedidos do cliente de id 3.
    8- Selecione o id do cliente e a data do pedido dos pedidos
     realizados no dia 15 de março de 2022.
