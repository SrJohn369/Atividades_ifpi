from Universidades import *


class Aluno:
    def __init__(self, cpf, nome, dt_nasc, matricula_uni_publica, matricula_uni_priv, pont_enem):
        self.__cpf = cpf
        self.__nome = nome
        self.__dt_nasc = dt_nasc
        self.__matricula_uni_publica = matricula_uni_publica
        self.__matricula_uni_priv = matricula_uni_priv
        self.__pont_enem = pont_enem

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def pont_enem(self):
        return self.__pont_enem

    @property
    def dt_nasc(self):
        return self.__dt_nasc

    def solicita_ingresso(self, curso: Curso, universidade: Universidade) -> bool:
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            pass
        else:
            pass

    def efetiva_matricula(self, curso: Curso, universidade: Universidade) -> bool:
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            pass
        else:
            pass

    def solicita_tranferencia(self, univ_origem: Universidade, curso_origem: Curso, univ_destino: Universidade):
        if isinstance(univ_origem, Universidade) and isinstance(curso_origem, Curso) \
            and isinstance(univ_destino, Universidade):
            pass
        else:
            pass
