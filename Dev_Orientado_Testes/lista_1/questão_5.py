"""Lista 01 - Questão 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via
parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7"""

# funçao do peso ideal
def peso_ideal(altura, sexo):
    # verificando se é homem ou mulher
    if sexo == 2:
        return (72.7 * altura) - 58
    elif sexo == 1:
        return (62.1 * altura) - 44.7

while True:
    try:
        altura = float(input("Digite sua altura: "))
        sexo = int(input("Digete 1 para feminino e 2 para masculido: "))
        peso_id = peso_ideal(altura, sexo)
        print(f'Seu peso ideal é de {peso_id:.2f}')
        break
    except:
        print("Valor para altura ou sexo inválido. Tente novamente!")
