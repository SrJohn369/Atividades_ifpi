""" Lista 01 - Questão 4 - Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um
procedimento que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você
foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)."""

def ler_media(nota1,nota2):
    media = (nota1+nota2) / 2
    if media >= 6:
        return f'PARABÉNS! Você foi aprovado! Sua média foi {media:.1f}'
    else:
        return f' Você não foi aprovado! Sua média foi {media:.1f}'

while True:
    try:
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        print(ler_media(nota1,nota2))
        break
    except:
        print('O que vocẽ digitou não é um número! Tente novamente')
