Comandos PSQL básicos
Fonte: https://www.postgresql.org/docs/15/app-psql.html

-- ver a versão do psql e se ele está instalado e no caminho de busca do SO
psql --version

--Conectar ao servidor com usuario específico
-- psql -h <endereço do host> -p <porta do Postgres> -U <usuário> -d <nome do banco> 
-- Exemplo para conectar ao servidor sem um banco específico
$ psql -h localhost -p 5432 -U postgres -W

-- listar os bancos de dados do servidor
\l 

-- conectar a um banco de dados
\c nome_do_banco 

-- listar os esquemas de um banco de dados
\dn 

-- Mostrar os caminhos de busca dos esquemas configurados
SHOW search_path; 

-- Configurar os esquemas para o caminho de busca
SET search_path TO myschema,public; 

-- listar as tabelas do banco conectado
-- se não especificar o esquema, serão mostradas as tabelas dos esquemas
-- que estão configurados no caminho de busca.
\dt 

-- listar todas as tabelas de todos os esquemas
\dt *.*

-- listar todas tabelas de um esquema específico
\dt schema.* 

-- ver a estrutura de uma tabela
\d nome_da_tabela

-- ver mais informações sobre uma tabela
\d+ nome_da_tabela

-- listar os usuários de um banco de dados
\du

-- ver informações sobre um usuário específico
\du nome_do_usuário

-- listar todas as funções
\df

-- listar todas as views
\dv

-- salvar todos os resultados em um arquivo
\o  --ao final \o novamente para parar de salvar no arquivo.

-- executar comandos a partir de uma arquivo
\i caminho_e_nome_do_arquivo
\f caminho_e_nome_do_arquivo

\q - sair do psql