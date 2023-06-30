"""
Alunos: João Victor de Sousa && Maria Eduarda Amarante && Carla Rejiane
"""


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
                print()
                return True
            else:
                return False
        else:
            return False

    def efetiva_matricula(self, curso, universidade):
        if isinstance(curso, Curso) and isinstance(universidade, Universidade):
            if self.solicita_ingresso(curso, universidade):
                if curso.vagas > 0 and curso.nome in universidade.cursos[curso.nome]:
                    curso.alunos.append(self)
                    print("matricula efetivada com sucesso!")
                else:
                    print(f"Não há vagas disponiveis ou o Curso {curso.nome} não existe na universidade desejada")
                    return ''
            else:
                print("Pontos insuficientes para ingressar no curso")
                return ''
        else:
            print('Um dos objetos fornecido não é instancia de Curso ou Universidade')
            return ''

    def solicita_tranferencia(self, univ_origem, curso_origem, univ_destino):
        if isinstance(curso_origem, Curso) \
                and isinstance(univ_origem, Universidade) \
                and isinstance(univ_destino, Universidade):
            if self in curso_origem.alunos \
                    and curso_origem.nome in univ_origem.cursos[curso_origem.nome] \
                    and curso_origem.nome in univ_destino.cursos[curso_origem.nome]:
                pass

            else:
                print('Não está matrículado no curso ou universidade informado curso não tem na universidade destino')
        else:
            print('Um dos objetos fornecido não é instancia de Curso ou Universidade')
            return ''


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
        for i, valor in enumerate(self.__alunos):
            if i == 0:
                str_alunos += f'CURSO: {self.nome}\n'
                str_alunos += '|'+5*'='+f' Alunos matriculados '+5*'='+'|'+f' Resta {self.vagas} vagas'+'\n'
            str_alunos += f'\tNome:\t{valor.nome}\n\t' \
                          f'CPF:\t{valor.cpf}\n\t' \
                          f'Enem:\t{valor.pont_enem}\n\t' + 25*'-' + '\n'
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
            print(f"ERROR: {curso} não é uma isntância de Curso!")


# ---------------------------------------------------------------------------------------------------------------------#
class Sisu:
    __univesidades = []

    @staticmethod
    def incluir_universidade(universidade):
        if isinstance(universidade, Universidade):
            Sisu.__univesidades.append(universidade)
        else:
            print(f"ERROR: {universidade} não é uma isntância de Universidade!")


if __name__ == '__main__':
    """
    Alunos: João Victor de Sousa && Maria Eduarda Amarante && Carla Rejiane
    """
    # --- Universidades
    universidades = [
        Universidade("UFPR", "Universidade Federal do Paraná", "Publica"),
        Universidade("Unila", "Universidade Federal da Integração Latino-Americana", "Privada"),
        Universidade("UTFPR", "Universidade Tecnológica Federal do Paraná", "Publica")
    ]
    # --- Alunos
    alunos = [
        Aluno("987.654.321-00", "Gabriel Fernandes", "12/12/2011", 820),
        Aluno("456.789.123-00", "Isabela Santos", "13/01/2012", 760),
        Aluno("789.123.456-00", "Bruno Oliveira", "14/02/2013", 790),
        Aluno("321.654.987-00", "Amanda Costa", "15/03/2014", 800)
    ]
    # --- Cursos
    cursos = [
        Curso(2, "Medicina", 6, 40, 850),
        Curso(4, "Direito", 5, 55, 700),
        Curso(5, "Psicologia", 5, 45, 720),
        Curso(6, "Arquitetura", 5, 30, 730),
        Curso(8, "Enfermagem", 4, 50, 690),
        Curso(10, "Economia", 4, 60, 670)
    ]
# ---------------------------------------------------------------------------------------------------------------------#
    #######TESTES#######

# ---------------------------------------------------------------------------------------------------------------------#
