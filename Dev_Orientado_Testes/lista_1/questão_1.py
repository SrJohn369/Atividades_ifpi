"""Lista 01- Questão 01- Faça um programa que contenha uma função que recebe um número inteiro por parâmetro e retorna 
verdadeiro se ele for par e falso se for ímpar."""
def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        numero = int(input("\nDigite um número: "))
        if par_ou_impar(numero):
            print(f'O número {numero} é par!')
            break
        else:
            print(f'O número {numero} é ímpar!')
            break
    except:
        print('O que você digitou não é um número inteiro. Tente novamente.')
