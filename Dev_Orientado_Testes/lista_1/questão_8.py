"""lista 1 Questão 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual
a 'S' ou 'N'. Se o caractere não for nem 'S', nem 'N', a função imprime a mensagem 'Caractere inválido. Digite
novamente'. Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo
na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou
não. """


def verificar():
    while True:
        caracter = input("Deseja continuar? Digite 'S' para Sim e 'N' para Não: ").upper()[0]
        # Verifica se o caractere é 'S' ou 'N'
        if caracter == 'S' or caracter == 'N':
            return caracter
        else:
            print("Caractere inválido. Digite novamente!")


print("DEIXANDO NÚMEROS VOLUMOSOS!!\n")
verific = 'S'
while verific == 'S':
    try:
        num = float(input("Digite um número qualquer: "))
        qua = num ** 3
        print(f"O cubo de {num} é {qua:.2f}")
        verific = verificar()
    except:
        print("Informe um valor válido!")
