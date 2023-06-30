from time import sleep


class Excessao(Exception):
    pass


def verfica(op):
    if 0 > op or op > 8:
        raise Excessao("Opção inexistente! Tente novamete")
    else:
        pass


while True:
    try:
        print(
                """OPÇÕES:
            0 - Encerrar Teste
            1 - Ligar Celular
            2 - Colocar Bateria
            3 - Ligar Wifi
            4 - Desligar Celular
            5 - Desligar Wifi
            6 - Assitir Vídeo
            7 - Carregar Celular
            8 - Trocar Bateria"""
            )
        opcao = int(input("Digite o número da opção desejada:\t"))
        verfica(opcao)
        if opcao == 0:
            break
    except ValueError as err:
        print(f"Opção inválida, Digite apenas NÚMEROS INTEIROS entre 0-8. Tente novamente!")
        sleep(4)
    except Excessao as err:
        print(err)
        sleep(4)
