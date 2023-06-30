"""1) Faça um programa que grave uma lista de 10 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista."""


def num_par(lista_var):
    lista_pares = lista_impar = []                                          # lista para guardar os pares
    for i in lista_var:                                                     # laço para cada eleemto da lista
        if i % 2 == 0:                                                      # verifica se é par
            lista_pares.append(i)                                           # adiciona a lista de pares
        else:
            lista_impar.append(i)                                           # adiciona a lista de imnpares
    return len(lista_pares), lista_pares, len(lista_impar), lista_impar     # retorna uma tupla com is valores


lista = []          # lista para guardar os 10 elementos
num_atual = 1       # conta o o número atual
count = 10          # inicio do for. Isso é usado para caso erre um, não precisse digitar os 10 novamente
while True:         # laço para verificar os testes try except
    try:
        for i in range(count):
            num = int(input(f"Digite o {num_atual}ª número inteiro:\t"))
            lista.append(num)
            num_atual += 1
            count -= 1
        # finaliza tudo
        break
    except:
        print("Error! Digite um valor numérico inteiro. Tente novamente!")
# No fim do laço mostra os resultados
# Mostre a quantidade de números pares
print(num_par(lista)[0], " --- Mostre a quantidade de números pares ")
# Grave uma lista somente com os números pares e mostre a lista
print(num_par(lista)[1], " --- Grave uma lista somente com os números pares e mostre a lista")
# Mostre a quantidade de números ímpares
print(num_par(lista)[2], " --- Mostre a quantidade de números ímpares")
# Grave uma lista somente com os números ímpares e mostre a lista
print(num_par(lista)[3], " --- Grave uma lista somente com os números ímpares e mostre a lista")
