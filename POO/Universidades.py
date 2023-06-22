class ErrorsClass(Exception):
    pass


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
            if self.pont_enem >= curso.nota_corte:
                return True
        else:
            return False

    def efetiva_matricula(self, curso, universidade) -> bool:
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            if self.__matricula_uni_publica is False:  # MATRICULA =========
                if self not in universidade.cursos[curso.nome].alunos:
                    if universidade.cursos[curso.nome].vagas > 0:
                        curso.cadastra_aluno(self)
                    else:
                        return f'Não há vagas no curso {curso.nome} na {universidade.nome}'
                else:
                    return 'Já está matriculado nesta universidade'
        else:
            raise ErrorsClass(f"ERROR: {curso} ou {universidade} não é uma instancia")

    def solicita_tranferencia(self, univ_origem, curso_origem, univ_destino):
        if isinstance(univ_origem, Universidade) and isinstance(curso_origem, Curso) \
                and isinstance(univ_destino, Universidade):
            if self in curso_origem and self in univ_origem:
                if curso_origem in univ_destino.cursos and univ_destino.cursos[curso_origem.nome].vagas > 0:
                    univ_origem.cursos[curso_origem.nome].alunos.drop(self)
                    univ_destino.cursos[curso_origem.nome].cadastra_aluno(self)
            else:
                return f'{self} não está em {curso_origem} ou {univ_origem}'
        else:
            raise ErrorsClass(f"ERROR: {univ_origem} ou {univ_destino} ou {curso_origem} não é uma instancia")


# ---------------------------------------------------------------------------------------------------------------------#
class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id
        self.__nome = nome
        self.__duracao = duracao
        self.__vagas = vagas
        self.__nota_corte = nota_corte
        self.__alunos = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def duracao(self):
        return self.__duracao

    @property
    def vagas(self):
        return self.__vagas

    @property
    def nota_corte(self):
        return self.__nota_corte

    @property
    def alunos(self):
        return self.__alunos

    @alunos.setter
    def alunos(self, valor):
        self.__vagas -= 1

    def __str__(self):
        str_alunos = ''
        for i in self.__alunos:
            str_alunos += f'Id:\t{i.id}\n\t' \
                          f'Nome:\t{i.nome}\n\t' \
                          f'Duração:\t{i.duracao}\n\t' \
                          f'Vagas:\t{i.vagas}\n\t' \
                          f'Nota de corte:\t{i.nota_corte}'
        return str_alunos

    def cadastra_aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
            self.__vagas -= 1
        else:
            pass


class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.__sigla = sigla
        self.__nome = nome
        self.__tipo = tipo
        self.cursos = {}

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        str_alunos = ''
        for i in self.cursos:
            str_alunos += f'Nome:\t{i.nome}\n\t' \
                          f'CPF:\t{i.cpf}\n\t' \
                          f'Nota no Enem:\t{i.pont_enem}\n\t' \
                          f'Data De Nascimento:\t{i.dt_nasc}\n\t'
        return str_alunos

    def cadastrar_curso(self, curso: Curso):
        if isinstance(curso, Curso):
            self.cursos[curso.nome] = curso
        else:
            raise ErrorsClass(f"ERROR: {curso} não é uma isntância de Curso!")


# ---------------------------------------------------------------------------------------------------------------------#
class Sisu:
    __univesidades = []

    @staticmethod
    def incluir_universidade(universidade):
        if isinstance(universidade, Universidade):
            Sisu.__univesidades.append(universidade)
        else:
            raise ErrorsClass(f"ERROR: {universidade} não é uma isntância de Universidade!")


if __name__ == '__main__':
    pass
# ---------------------------------------------------------------------------------------------------------------------#
