CREATE TABLE cliente(
	cpf numeric(11,0) primary key,
	rg numeric(14,0) NOT NULL UNIQUE,
	nome varchar(30) NOT NULL,
	data_nascimento date NOT NULL,
	ativo boolean DEFAULT true
);
INSERT INTO cliente VALUES 
(111111,12345,'Antonio','2000/10/25', false),
(111222,12350,'Maria','2001/11/25', true),
(222222,15423,'João','1999/06/23', true),
(333333,54321,'Ana Maria','2003/05/12',null),
(444444,51423,'Bela','2003/09/30',null),
(555555,12354,'Livia','2002/12/23',true)
(666666,51243,'Anacleto','2003/06/12',false);

CREATE TABLE pedido (
  id INT PRIMARY KEY,
  data DATE,
  valor NUMERIC(10,2),
  cliente_id INT,
  FOREIGN KEY (cliente_id) REFERENCES cliente(cpf)
);

INSERT INTO pedido (id, data, valor, cliente_id) VALUES
  (1, '2021-01-05', 100.00, 111111),
  (2, '2021-02-12', 50.00, 111222),
  (3, '2021-03-10', 200.00, 111111),
  (4, '2021-03-15', 75.00, 222222),
  (5, '2021-04-02', 150.00, 111222);

/*
COMANDO SELECT
SINTAXE: 
SELECT [ * | EXPRESSÃO] FROM TABELA
*/

--TODOS OS ATRIBUTOS
SELECT * FROM cliente;

--ATRIBUTOS ESPECÍFICOS
SELECT cpf, nome FROM cliente;

--ATRIBUTOS ESPECÍFICOS E FILTRO
SELECT cpf, nome FROM cliente WHERE ativo=true;
ou
SELECT cpf, nome FROM cliente WHERE ativo;

--CLÁUSULA DISTINCT 
--ELIMINAR RESULTADOS REPETIDOS
-- Mostrar os cpf de todos os clientes que efetuaram pedido
SELECT cliente_id FROM pedido;

SELECT DISTINCT cliente_id FROM pedido;

/*
OPERADORES DE COMPARAÇÃO
> - MAIOR
>= - MAIOR OU IGUAL
< - MENOR
<= - MENOR OU IGUAL
= - IGUAL
<> ou != - DIFERENTE

OPERADORES LÓGICOS
AND - e
OR - ou

OPERADORES ESPECIAIS - Utilizados para campos que recebem valor NULO.
IS NULL - é nulo
IS NOT NULL - não é nulo
*/
SELECT * FROM cliente WHERE ativo IS NULL;

SELECT * FROM cliente WHERE ativo IS NOT NULL;


/*
OPERADOR IN
Utilizado quando desejamos consultar uma tabela, filtrando
o valor de um dos campos a partir de uma lista de possibilidade.
*/
SELECT * 
FROM cliente 
WHERE nome = 'Ana' OR nome = 'Maria' OR nome = 'João';

SELECT *
FROM cliente
WHERE nome IN ('Ana','Maria','João');

/*
OPERADOR BETWEEN
Usado quando precisamos recuperar as linhas de uma 
tabela cujo valor de um campo encontra-se em um 
intervalo específico.
*/
SELECT * FROM pedido WHERE data >= '2021-03-01' AND data <= '2021-03-31';

SELECT * FROM pedido WHERE data BETWEEN '2021-03-01' AND '2021-03-31';

/*
OPERADOR LIKE
Utilizado para buscar por uma determinada string
dentro de um campo com valores textuais
% -> curinga para qualquer conjunto de zero ou vários caracteres
_ -> curinga para UM caractere qualquer
*/
SELECT * FROM cliente WHERE nome LIKE 'Ana%';

SELECT * FROM cliente WHERE nome LIKE '%Maria%';

/*
OPERADOR SIMILAR TO
Extende o LIKE, adicionando mais opções:
% ou _ -> Mesmo significado do uso com LIKE
[A-F] -> Representa qualquer caractere entre A e F
[AEF] -> Representa exatamente os caracteres A, E e F
[^AEF] -> Significa qualquer caractere diferente de A, E e F
*/
SELECT * FROM cliente WHERE nome SIMILAR TO '[AB]%';

SELECT * FROM cliente WHERE nome SIMILAR TO '[A-J]%';

/*
CLÁUSULA ORDER BY
Esta cláusula retorna os registros de uma tabela 
ordenados de acordo com uma expressão especificada
[ASC]
DESC
*/
SELECT * FROM cliente ORDER BY nome;

SELECT * FROM pedido ORDER BY valor DESC;

/*
CLÁUSULA LIMIT
Esta cláusula retorna apenas alguns registros de uma
tabela de acordo com uma expressão especificada

LIMIT número
LIMIT OFFSET número

*/

SELECT * FROM cliente LIMIT 2;

SELECT * FROM cliente LIMIT 2 OFFSET 2;


EXERCÍCIOS:



