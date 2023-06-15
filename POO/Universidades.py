from Cursos import *


class Sisu:
    __univesidades = []

    @staticmethod
    def incluir_universidade(universidade):
        Sisu.__univesidades.append(universidade)


class Universidade:
    def __int__(self, sigla: str, nome: str, tipo: str, cursos: list):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.__cursos = cursos

    def __str__(self):
        for i, valor in enumerate(self.__cursos):
            if i == 0:
                print(f"Universidade:\t{self.__nome}({self.__sigla})\n"
                      f"Tipo:\t{self.__tipo}\n"
                      f"Curso:\n")
            else:
                print(i + f' - {valor}')

    def cadastrar_curso(self, curso: Curso):
        if isinstance(curso, Curso):
            self.__cursos.append(curso.nome)
        else:
            pass
