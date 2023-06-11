"""Lista 01 - questão 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial,
sabemos que N! depende de ( N-1)!; este por sua vez depende de (N-2)!; e, assim por diante, até que N seja 1,
quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o
número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro. """


def fatorial(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat *= i
    return fat


while True:
    try:
        numero = int(input("Digite um número: "))
        print(f"o fatorial de {numero} é {fatorial(numero)}")
    except:
        print("Valor inválido, por favor digite un número inteiro. Tente novamente")
