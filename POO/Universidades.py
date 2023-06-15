class Aluno:
    def __init__(self, cpf, nome, dt_nasc, pont_enem, matricula_uni_publica=False, matricula_uni_priv=False):
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

    def solicita_ingresso(self, curso, universidade) -> bool:
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            pass
        else:
            pass

    def efetiva_matricula(self, curso, universidade) -> bool:
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            pass
        else:
            pass

    def solicita_tranferencia(self, univ_origem, curso_origem, univ_destino):
        if isinstance(univ_origem, Universidade) and isinstance(curso_origem, Curso) \
                and isinstance(univ_destino, Universidade):
            pass
        else:
            pass


class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id
        self.__nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.__nota_corte = nota_corte
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        str_alunos = ''
        for i in self.__alunos:
            str_alunos += f'Nome:\t{i.nome}\n\t' \
                          f'CPF:\t{i.cpf}\n\t' \
                          f'Nota no Enem:\t{i.pont_enem}\n\t' \
                          f'Data De Nascimento:\t{i.dt_nasc}\n\t'
        return f"\t\t\t{self.__nome}\n" \
               f"Id:\t\t{self.__id}\n" \
               f"Duração:\t{self.__duracao}\n" \
               f"Vagas:\t{self.__vagas}\n" \
               f"Nota de corte:\t{self.__nota_corte}\n" \
               f"Alunos matriculados:\n\t{str_alunos}"

    def cadastra_aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
        else:
            pass


class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.__cursos = []

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


class Sisu:
    __univesidades = []

    @staticmethod
    def incluir_universidade(universidade):
        Sisu.__univesidades.append(universidade)


if __name__ == '__main__':
    pass
