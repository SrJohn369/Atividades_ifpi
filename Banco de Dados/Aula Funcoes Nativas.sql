/*FUNÇÕES NATIVAS (usar banco empresa)
Informações do sistema e de sessão
Obter versão do SGBD, data/hora do sistema, usuário e database atuais.*/

--Retorna a versão do PostgreSQL
SELECT version();
--Retorna a data e hora atual do Servidor
SELECT now();
--Retorna o usuário atual
SELECT current_user;
--Retorna a banco de dados conectado
SELECT current_database();

--Manipulação de data/hora
/*Obter data e hora atuais e 
obter partes do timestamp 
(Padrão SQL-2003).*/
SELECT current_date, 
	   current_time, 
	   localtimestamp;

/*EXTRACT(field FROM timestamp)
Onde field pode ser qualquer um dos seguintes identificadores:
century, day, decade
dow / isodow: dia da semana
sendo Sunday(0/1) to Saturday(6/7)
doy: dia do ano (1: 365/366)
epoch, hour, microseconds, millennium
milliseconds, minute, Month, quarter
second, timezone, timezone_hour, timezone_minute
week, year / isoyear*/

-- Uso de operador para calcular a 
-- diferença de anos.
SELECT pnome,
EXTRACT(YEAR FROM NOW()) –
EXTRACT(YEAR FROM datanasc)
AS idade
FROM empregado;

--Função AGE
SELECT pnome, AGE(datanasc) AS idade
FROM empregado;

--Função DATE_PART utiliza os mesmos 
--identificadores de EXTRACT
--DATE_PART(text, timestamp)

SELECT EXTRACT(CENTURY FROM NOW()) as seculo,
	   DATE_PART('doy', NOW()) as diasano, 
	   DATE_PART('day', NOW()) as diaatual,
	   DATE_PART('hour', NOW()) as hora, 
	   DATE_PART('month', NOW()) as mesatual,
	   DATE_PART('epoch', NOW()) as seconds;

--Calcular nova data a partir de um 
--intervalo específico:
SELECT date '2022-11-10' AS compra,
date '2022-11-10' + 30 AS vencimento;

--Calcular intervalo de dias entre datas.
SELECT date '2014-03-28' - 
	   date '2014-03-12' as diferenca;

--Calcular intervalo de tempo entre horas, minutos e segundos.
SELECT time '05:00:30' - 
	   time '03:00:46';
--Calcular novo tempo a partir de intervalo
SELECT timestamp '2001-09-28 23:00' – 
       interval '28 hours';

SELECT 500 * interval '1 second';

--Manipulação de String
--Concatenação: operador ||.
SELECT pnome || ' ' || inicialm || '. ' || unome
AS “Nome Completo” FROM empregado;

--Conversão caixa alta–UPPER e caixa baixa-LOWER.
SELECT UPPER('banco'), LOWER('BANCO');

SELECT * 
FROM empregado
WHERE UPPER(pnome) = 'JOAO';

SELECT * 
FROM empregado
WHERE LOWER(pnome) = 'joao';

--Busca de string em caixa alta ou baixa
-- Função ILIKE (nativa postgres)
SELECT  * from  empregado
where pnome ILIKE 'JOAO';

--Obter número de caracteres em uma string 
--(length).
SELECT CHAR_LENGTH('banco '); -- 6

--Converte a 1ª letra de cada palavra em 
--caixa alta.
SELECT INITCAP('oi MUNDO');


/*Extensão UNACCENT
O unaccent é um dicionário de pesquisa de 
texto que remove os acentos (sotaques) dos lexemes. 
É um dicionário de filtragem, isso permite o processamento
insensível ao acento/sotaque para pesquisa 
completa de texto.*/

CREATE extension unaccent;

SELECT unaccent('sebastião');

SELECT * FROM empregado
where unaccent(pnome) ILIKE 'joao';

SELECT *
FROM empregado
WHERE UNACCENT(endereco) ILIKE '%ceara%';

--Manipulação de números

Operador Descrição 			Exemplo   Resultado
+ 	  adição    			2 + 3   	=5
– 	  subtração 			2 – 3   	=1
* 	  multiplicação 		2 * 3	 	=6
/ 	  divisão (divisão 
	  inteira trunca o 
	  resultado 			04/fev  	=2
% 	  módulo (resto) 		5 % 4 	 	=1
^ 	  exponenciação 		2.0 ^ 3.0 	=8
|/ 	  raiz quadrada 		|/ 27.0 	=5
||/ 	  raiz cúbica 		||/ 27.0 	=3
! 	  fatorial 				5 ! 		=120
!! 	  fatorial (operador
	  de prefixo) 			!! 5 		=120
@ 	  Valor absoluto 		@ - 5.0 	=5
& 	  AND bit a bit 		91 & 15 	=11
| 	  OR bit a bit 			32 | 3 		=35
# 	  XOR bit a bit 		17 # 5 		=20
~ 	  NOT bit a bit 		~ 1 		=-2
<< 	  deslocamento à 
	  esquerda bit a bit 	1 << 4 		16
>> 	  deslocamento à 
	  direita bit a bit 	20 >> 4 	1

-- FUNÇÕES
Função Descrição Exemplo Resultado
abs() valor absoluto abs(-17.4) 17.4
cbrt() raiz cúbica cbrt(27.0) 3
ceil() o menor inteiro não menor que
o argumento ceil(-42.8) -42
exp() exponenciação exp(1.0) 2.71828182845905
floor() o maior inteiro não maior que o
argumento floor(-42.8) -43
log() logaritmo na base 10 log(100.0) 2
mod(x,y) resto de y/x mod(9,4) 1
pi() constante “π” pi() 3.14159265358979
power(a,b) a elevado a b power(9.0, 3.0) 729
random() valor randômico entre 0.0 e 1.0 random()
round() arredondar para o inteiro mais
próximo round(42.4) 42
round(v,s) arredondar para s casas decimais
round(42.4382, 2) 42.44
setseed() define a semente para as chamadas
a random() setseed(0.54823) 1177314959
sqrt() raiz quadrada sqrt(2.0) 1.4142135623731
trunc() trunca em direção ao zero trunc(42.8) 42
trunc(v,s) trunca com s casas decimais trunc(42.4382, 2) 42.43

