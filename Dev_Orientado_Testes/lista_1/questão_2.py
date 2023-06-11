"""Lista 1 - Questão 2 - Escreva um programa que leia o raio de m círculo e faça duas fuções: uma função chamada área
que calcula e retorna a área do circulo e outra função chamada perímetro que calcula e retorna o perímetro do circulo.
Área = pi * r^2
Perímetro = pi * 2 * r"""

def area(raio):
    return 3.14 * raio ** 2
def perimetro(raio):
    return 3.14 * 2 * raio

while True:
    try:
        raio = int(input("\nDigite o raio do circulo(número inteiro): "))
        print(f"\nA Área do circulo é {area(raio):.2f}")
        print(f"\nO Perímetro do circulo é {perimetro(raio):.2f}")
        break
    except:
        print("O que você digitou não é um número inteiro. Tente novamente!")
