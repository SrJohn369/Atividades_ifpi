# 'create_engine' função para criar uma instância de mecanismo de banco de dados
# 'SQLModel' classe que fornece funcionalidades de modelo de dados
# 'decouple' biblioteca que ajuda a gerenciar configurações em arquivos separados
# 'config' é uma forma conveniente de carregar configurações de variáveis de ambiente de um arquivo .env e acessá-las no código
from sqlmodel import create_engine, SQLModel
from decouple import config


def obter_engine():
    '''criar e retornar uma instância de mecanismo de banco de dados para uma conexão com o PostgreSQL'''
    
    HOST = config('DB_HOST')
    PORT = config('DB_PORT')
    DB = config('DB_DATABASE')
    USER = config('DB_USER')
    PASSWORD = config('DB_PASSWORD')
    url_db = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    #  'echo=True' permite que o mecanismo exiba informações de depuração.
    engine = create_engine(url_db, echo=True)
    return engine


def criar_tabelas():
    engine = obter_engine()
    SQLModel.metadata.create_all(engine)