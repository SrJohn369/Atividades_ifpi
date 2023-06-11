"""Lista 1 Questão 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO."""


def calcular_poligono(lados, medida):
    if lados == 3:
        perimetro_t = 3 * medida
        return f'O poligono é um triângulo e seu perimetro é de {perimetro_t:.2f}cm!'
    elif lados == 4:
        area = medida ** 2
        return f'O poligono é um quadrado e o valor de sua área é de {area:.2f}cm ao quadrado!'
    elif lados == 5:
        return f'O poligono é um pentágono!'


while True:
    try:
        n_Lados = int(input("Digite o número de lados do polígono regular: "))
        m_Lado = float(input("Digite a medida do lado desse polígono(em cm): "))
        print(calcular_poligono(n_Lados, m_Lado))
        break
    except:
        print(f'O valor para quantidade de lados ou a media do lago está inválido. Tente novamente!')
