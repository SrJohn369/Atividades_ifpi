/*
AULA MULTIPLAS TABELAS E FUNÇÕES AGREGAÇÃO
*/

--Inner Join com Using (usando banco Livraria)
--Clientes que fizeram algum pedido
select nome 
from clientes INNER JOIN pedidos using (cod_cliente);

-- Natural Join
select nome 
from clientes natural join pedidos;

-- Inner join / Natural join com Distinct
SELECT DISTINCT nome 
FROM clientes NATURAL JOIN pedidos;

select distinct nome 
from clientes inner join pedidos 
			on clientes.cod_cliente = pedidos.cod_cliente;


--TODO SELECT responde duas perguntas?
-- 1) O que retornar na consulta?
-- 2) Qual a condição?

--Quais clientes fizeram pedido no dia 06/06/2001?
SELECT c.nome, p.data_pedido
FROM clientes c NATURAL JOIN pedidos p
WHERE p.data_pedido = '06/06/2001';

SELECT c.nome, p.data_pedido 
FROM clientes c INNER JOIN pedidos p
				USING (cod_cliente)
WHERE p.data_pedido = '06/06/2001';


-- Quais os livros foram pedidos pelo 
-- Gilberto Ribeiro de Queiroz no dia 06/06/2001?
-- NATURAL JOIN
SELECT l.titulo
FROM clientes c NATURAL JOIN pedidos p
			  NATURAL JOIN pedidoslivros pl
			  NATURAL JOIN livros l
WHERE c.nome = 'Gilberto Ribeiro de Queiroz' AND
	  p.data_pedido = '06/06/2001';
	
-- JOIN COM USING	 
SELECT l.titulo
FROM clientes c INNER JOIN pedidos p USING (cod_cliente)
			    INNER JOIN pedidoslivros pl USING (num_pedido)
			    INNER JOIN livros l USING (isbn)
WHERE c.nome = 'Gilberto Ribeiro de Queiroz' AND
	  p.data_pedido = '06/06/2001';
	  
-- JOIN COM ON
SELECT l.titulo
FROM clientes c INNER JOIN pedidos p        ON c.cod_cliente = p.cod_cliente
			    INNER JOIN pedidoslivros pl ON p.num_pedido = pl.num_pedido
			    INNER JOIN livros l         ON pl.isbn = l.isbn
WHERE c.nome = 'Gilberto Ribeiro de Queiroz' AND
	  p.data_pedido = '06/06/2001';


-- FUNÇÕES DE AGREGAÇÃO
-- COUNT
-- Quantos pedidos foram realizados?
SELECT COUNT(*) 
FROM pedidos;

-- Quantos pedidos foram realizados com 
-- Valor Pago maior que R$ 100,00?
SELECT COUNT(*) 
FROM pedidos
WHERE total_pago > 100;

-- Quantos clientes do sexo masculino 
-- existem na livraria?
SELECT COUNT(*)
FROM clientes
WHERE sexo = 'M';

-- MIN e MAX
-- Qual o menor valor pago em um pedido?
SELECT MIN(total_pago) 
FROM pedidos;

-- Qual o maior valor pago em um pedido?
SELECT MAX(total_pago) 
FROM pedidos;

-- Qual o nome do 1o. cliente em ordem alfabética?
SELECT MIN(nome)
FROM clientes;

SELECT nome
FROM clientes
ORDER BY nome LIMIT 1;

-- Qual o nome do último cliente em ordem alfabética?
SELECT MAX(nome) 
FROM clientes;

-- Qual o valor do livro mais barato?
SELECT MIN(preco) 
FROM livros;

-- Qual o valor do livro mais caro?
SELECT MAX(preco) 
FROM livros;

-- SUM
-- Quanto a livraria arrecadou com todos os pedidos?
SELECT SUM(total_pago) 
FROM pedidos;

-- Quanto o cliente Gilberto Ribeiro de Queiroz 
-- já gastou com a livraria?
SELECT SUM(total_pago) 
FROM pedidos INNER JOIN clientes USING (cod_cliente)
WHERE nome = 'Gilberto Ribeiro de Queiroz';

-- AVG
-- Qual a média dos valores pagos em todos os pedidos?
SELECT AVG(total_pago) 
FROM pedidos;

-- Qual a média dos preços dos livros cadastrados?
SELECT AVG(preco)
FROM livros;

-- Qual a média de preços dos livros 
-- de Machado de Assis?
SELECT AVG(preco)
FROM livros INNER JOIN autoreslivros USING(isbn)
            INNER JOIN autores USING(cod_autor)
WHERE nome = 'Machado de Assis';

SELECT AVG(preco)
FROM livros INNER JOIN autoreslivros USING(isbn)
            INNER JOIN autores USING(cod_autor)
WHERE nome ILIKE 'machado de assis';

--Qual a idade média dos livros
SELECT AVG((current_date - data_publicacao)/365) as anos
FROM livros;

-- GROUP BY
-- Qual a quantidade de livros por categoria?
-- Visualizando o codigo da categoria
SELECT cod_categoria, COUNT(*)
FROM livros
GROUP BY cod_categoria;

-- Visualizando a descrição da categoria
SELECT desc_categoria, COUNT(*)
FROM livros INNER JOIN categorialivros 
             USING(cod_categoria)
GROUP BY desc_categoria;

-- Qual a quantidade de livros por autor?
SELECT nome, COUNT(*)
FROM livros INNER JOIN autoreslivros USING(isbn)
            INNER JOIN autores USING(cod_autor)
GROUP BY nome;

-- Qual a quantidade de clientes por sexo?
SELECT sexo, COUNT(*)
FROM clientes
GROUP BY sexo;

-- Qual a média de valores dos livros por editora
-- ordenado pelo preço médio
SELECT nome, AVG(preco) Preco_Medio
FROM livros INNER JOIN editoras USING(cod_editora)
GROUP BY nome
ORDER BY Preco_Medio;

-- HAVING (filtrar grupos)
-- Qual o nome do cliente que fez mais de um pedido?
SELECT nome, COUNT(*) qtd_pedido
FROM clientes INNER JOIN pedidos
              USING(cod_cliente)
GROUP BY nome
HAVING COUNT(*) > 1;




