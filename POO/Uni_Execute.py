from Universidades import *

# --- Universidades
universidade = [
    Universidade("UFPR", "Universidade Federal do Paraná", "Publica"),
    Universidade("Unila", "Universidade Federal da Integração Latino-Americana", "Privada"),
    Universidade("UTFPR", "Universidade Tecnológica Federal do Paraná", "Publica"),
    Universidade("UEMS", "Universidade Estadual do Mato Grosso do Sul", "Privada")]
# --- Alunos
aluno = [
    Aluno("123.456.789-10", "Lucas da Silva", "15/02/1998", 780, matricula_uni_priv=True),
    Aluno("987.654.321-20", "Beatriz Oliveira", "10/07/2001", 820, matricula_uni_priv=True),
    Aluno("456.789.123-30", "Rafael Santos", "03/11/1995", 750, matricula_uni_publica=True),
    Aluno("321.654.987-40", "Júlia Ferreira", "27/05/2000", 790, matricula_uni_publica=True)]
# --- Cursos
curso = [
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


curso[0].cadastra_aluno(aluno[0])
curso[0].cadastra_aluno(aluno[2])
test = curso[0]
print(test)
