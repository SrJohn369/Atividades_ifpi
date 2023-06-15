from Aluno import *


class Curso:
    def __init__(self, id: int, nome: str, duracao: int, vagas: int, nota_corte: int, alunos: list):
        self.__id = id
        self.__nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.__nota_corte = nota_corte
        self.__alunos = alunos

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        print()

    def cadastra_aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
        else:
            pass