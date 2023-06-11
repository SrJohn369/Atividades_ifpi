CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nome VARCHAR(50),
  idade INT,
  cidade VARCHAR(50)
);

CREATE TABLE pedidos (
  id INT PRIMARY KEY,
  data DATE,
  valor DECIMAL(10,2),
  cliente_id INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Inserir dados na tabela clientes
INSERT INTO clientes (id, nome, idade, cidade)
VALUES (1, 'João Silva', 30, 'São Paulo'),
       (2, 'Maria Souza', 25, 'Rio de Janeiro'),
       (3, 'Pedro Almeida', 40, 'Belo Horizonte'),
       (4, 'Ana Costa', 35, 'Porto Alegre'),
       (5, 'Lucas Oliveira', 28, 'Salvador'),
       (6, 'Juliana Santos', 32, 'Curitiba'),
       (7, 'Rafaela Pereira', 27, 'Recife'),
       (8, 'Gustavo Lima', 31, 'Fortaleza'),
       (9, 'Carolina Fernandes', 29, 'Manaus'),
       (10, 'Fernando Cardoso', 33, 'Porto');

-- Inserir dados na tabela pedidos, referenciando a tabela clientes
INSERT INTO pedidos (id, data, valor, cliente_id)
VALUES (1, '2023-01-01', 100.00, 1),
       (2, '2023-02-05', 50.00, 2),
       (3, '2023-03-10', 200.00, 3),
       (4, '2023-04-15', 150.00, 4),
       (5, '2023-03-20', 80.00, 5),
       (6, '2023-03-25', 120.00, 6),
       (7, '2023-03-30', 300.00, 7),
       (8, '2022-08-05', 40.00, 8),
       (9, '2022-09-10', 250.00, 9),
       (10, '2022-10-15', 90.00, 10),
       (11, '2022-11-20', 60.00, 1),
       (12, '2022-12-25', 180.00, 2),
       (13, '2022-01-01', 200.00, 3),
       (14, '2022-02-05', 75.00, 4),
       (15, '2022-03-10', 150.00, 5),
       (16, '2022-04-15', 50.00, 6),
       (17, '2022-05-20', 100.00, 7),
       (18, '2022-06-25', 300.00, 8),
       (19, '2022-07-30', 70.00, 9),
       (20, '2022-08-05', 180.00, 10);
	   
--Lista de Exercícios Intemediário (AGREGAÇÕES E JOINS)
--1-Selecionar o nome e a idade dos clientes com idade maior que 30 anos.
SELECT nome, idade 
FROM clientes
WHERE idade > 30;

--2-Selecionar o nome e o id dos clientes que não moram em São Paulo.
SELECT nome, id, cidade
FROM clientes
WHERE cidade NOT ILIKE 'São Paulo';
   
--3-Selecionar o valor médio dos pedidos.
SELECT AVG(valor)
FROM pedidos;

--4-Selecionar a soma total dos valores de todos os pedidos:
SELECT SUM(valor)
FROM pedidos;

--5-Mostrar o nome do cliente e o valor total dos pedidos realizados por cada cliente.
SELECT c.nome, SUM(p.valor)
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nome;
	
--6-Selecionar o nome e a cidade dos clientes que realizaram pelo menos 
--um pedido com valor maior que R$ 100, ordenando por cidade.
SELECT DISTINCT c.nome, c.cidade
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE p.valor > 100
ORDER BY cidade;
	
--7-Selecionar o nome e a idade dos clientes que realizaram pelo 
--menos um pedido nos meses de janeiro, fevereiro ou março de 2023.
SELECT DISTINCT nome, idade, p.data
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE EXTRACT(MONTH FROM p.data) IN (1,2,3) AND 
      EXTRACT(YEAR FROM p.data) = 2023;
	
--8-Selecionar o nome do cliente e o valor médio dos pedidos realizados por cada cliente.
SELECT c.nome, ROUND(AVG(p.valor),2) as Media
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY nome
ORDER BY Media DESC;
	
	
--9-Selecionar o nome e a idade dos clientes que não realizaram nenhum pedido.
SELECT nome, idade
FROM clientes c LEFT JOIN pedidos p ON c.id = p.cliente_id
WHERE p.id IS NULL;
	
--10-Selecionar o nome do cliente e a data do primeiro pedido realizado 
--por cada cliente.
SELECT c.nome, MIN(p.data) as data_pedido
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nome
ORDER BY data_pedido;
	
--11-Mostrar o valor total de todos os pedidos agrupados por data.
SELECT data, SUM(valor)
FROM pedidos
GROUP BY data;


--12-Selecionar o nome do cliente, a data do pedido e o valor do pedido 
--dos pedidos realizados entre as datas 01/03/2023 e 31/03/2023.
SELECT c.nome, p.data, p.valor
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE p.data BETWEEN '01/03/2023' AND '31/03/2023';

--13-Selecionar a data e o valor dos pedidos feitos por clientes 
--com idade maior que 30
SELECT p.data, p.valor
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE c.idade > 30;

--14-Selecionar o valor mínimo e máximo dos pedidos:
SELECT MIN(valor), MAX(valor)
FROM pedidos;

--15-Selecionar o nome, a cidade e o valor total dos pedidos feitos 
--por cada cliente
SELECT c.nome, c.cidade, SUM(p.valor)
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nome, c.cidade;  

--16-Selecionar a idade média dos clientes que fizeram pedidos 
--com valor superior a 100
SELECT AVG(idade)
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE p.valor > 100;

--17- Selecionar o cliente que fez o pedido de menor valor
SELECT nome
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id
ORDER BY p.valor ASC
LIMIT 1;
