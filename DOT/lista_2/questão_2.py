"""2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista."""
# import random

"""Aqui poderá ser gerado automaticamente uma lista com 10 números reais 
explicando a sintaxe: vamos criar uma lista chamada lista_num_real que receberar uma COMPREENSÃO DE LISTA ou GERADOR
o valor desse gerador será um do tipo floate já que queremos uma número real, como não queremos um arredondamento termos
que formatar em uma string por isso usamos a função float para converter de string para float, e usando a biblioteca
radom no método uniform podemos definir quais números queremos gerar e então 'truncamos' em duas casas decimais
usando a formatação de strings e então usamos o laço for para definirmos quantos números queremos gerar na lista"""
# lista_num_real = [float(f"{random.uniform(-100, 100):.2f}") for i in range(10)]

# programa que grave uma lista com dez números reais
lista_num_real = []  # lista com os valores reais
num_atual = 1        # conta o o número atual
count = 10           # inicio do for. Isso é usado para caso erre um, não precisse digitar os 10 novamente
while True:          # laço para verificar os testes try except
    try:
        for i in range(count):
            num = float(input(f"Digite o {num_atual}ª número inteiro:\t"))
            lista_num_real.append(num)
            num_atual += 1
            count -= 1
        # finaliza tudo
        break
    except:
        print("Error! Digite um valor numérico real. Tente novamente!")

# calcule e mostre a quantidade de números negativos
lista_neg = []
soma_postv = 0
for j in lista_num_real:
    if j < 0:
        lista_neg.append(j)
    else:
        soma_postv += j
print(len(lista_neg), " -- Números negativos")
print(soma_postv, " -- Soma dos números positivos")
