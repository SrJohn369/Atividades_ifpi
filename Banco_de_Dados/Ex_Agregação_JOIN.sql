--Lista de Exercícios Intemediário (AGREGAÇÕES E JOINS)

--1-Selecionar o nome e a idade dos clientes com idade maior que 30 anos.
SELECT nome, idade
FROM clientes 
WHERE idade > 30;

--2-Selecionar o nome e o id dos clientes que não moram em São Paulo.
SELECT nome, id 
FROM clientes 
WHERE cidade!='São Paulo';
------------------------------------------------------
SELECT nome, id, cidade
FROM clientes
WHERE cidade NOT ILIKE 'São Paulo';

--3-Selecionar o valor médio dos pedidos.
SELECT AVG(valor) AS media
FROM predidos;


