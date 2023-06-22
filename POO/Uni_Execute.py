from Universidades import *
import os

# --- Universidades
universidades = [
    Universidade("UFPR", "Universidade Federal do Paraná", "Publica"),
    Universidade("Unila", "Universidade Federal da Integração Latino-Americana", "Privada"),
    Universidade("UTFPR", "Universidade Tecnológica Federal do Paraná", "Publica"),
    Universidade("UEMS", "Universidade Estadual do Mato Grosso do Sul", "Privada")]
# --- Alunos
alunos = [
    Aluno("888.888.888-88", "Juliana Costa", "08/08/2007", 760, matricula_uni_priv=True),
    Aluno("999.999.999-99", "Fernando Pereira", "09/09/2008", 830, matricula_uni_publica=True),
    Aluno("000.000.000-00", "Patrícia Lima", "10/10/2009", 700, matricula_uni_priv=True),
    Aluno("123.456.789-00", "Rafaela Mendes", "11/11/2010", 780, matricula_uni_publica=True),
    Aluno("987.654.321-00", "Gabriel Fernandes", "12/12/2011", 820, matricula_uni_priv=True),
    Aluno("456.789.123-00", "Isabela Santos", "13/01/2012", 760, matricula_uni_publica=True),
    Aluno("789.123.456-00", "Bruno Oliveira", "14/02/2013", 790, matricula_uni_priv=True),
    Aluno("321.654.987-00", "Amanda Costa", "15/03/2014", 800, matricula_uni_publica=True)]
# --- Cursos
cursos = [
    Curso(1, "Engenharia Civil", 5, 50, 750),
    Curso(2, "Medicina", 6, 40, 850),
    Curso(3, "Administração", 4, 60, 650),
    Curso(4, "Direito", 5, 55, 700),
    Curso(5, "Psicologia", 5, 45, 720),
    Curso(6, "Arquitetura", 5, 30, 730),
    Curso(7, "Engenharia de Software", 4, 35, 780),
    Curso(8, "Enfermagem", 4, 50, 690),
    Curso(9, "Ciências da Computação", 4, 40, 760),
    Curso(10, "Economia", 4, 60, 670)]


def aluno():
    def methods(instancia):
        while True:
            os.system('cls')
            print(
                """
                1 - Solicitar Entrada
                2 - Efetivar Matricula
                3 - Solicitar Transferencia
                999 - Voltar"""
            )
            try:
                opt_func = int(input("Opção:\t"))
                if opt_func == 1:
                    pass
                elif opt_func == 2:
                    pass
                elif opt_func == 3:
                    pass
                elif opt_func == 999:
                    break
            except:
                print(f"Valor inválido, apenas 1-3 ou 999. aperte enter tecla para tentar novamente...")
                input()

    while True:
        os.system('cls')
        print("Instancias de alunos:\n")
        for i, aluno in enumerate(alunos):
            print(f"{i} - Aluno: {alunos[i].nome} \tCPF: {alunos[i].cpf} \tENEM: {alunos[i].pont_enem}")
        print()
        print("999 - Voltar")
        try:
            opt_aluno = int(input("Opção:\t"))
            if opt_aluno != 999:
                methods(alunos[opt_aluno])
            else:
                break
        except:
            print(f"Valor inválido, apenas 0-{len(alunos)-1}. aperte enter tecla para tentar novamente...")
            input()


def main():
    while True:
        os.system('cls')
        print(
            """Menu de Testes
            Escolha a Instância:
            1 - Alunos
            2 - Universidade
            3 - Cursos
            4 - Finalizar """
        )
        try:
            opt = int(input("Opção:\t"))
            if opt == 1:
                aluno()
            elif opt == 2:
                pass
            elif opt == 3:
                pass
            elif opt == 4:
                print('Finalizado!')
                break
        except:
            print("Valor inválido, apenas 1-4. aperte enter tecla para tentar novamente...")
            input()


if __name__ == '__main__':
    main()