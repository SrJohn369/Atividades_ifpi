"""3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário."""


def primo(valor):
    if not isinstance(valor, int):
        return Exception
    # Um número é considerado primo se ele for maior que 1 e
    # tiver apenas dois divisores: o número 1 e ele mesmo
    elif valor <= 1:
        return Exception

    cont = 0
    for i in range(1, valor + 1):
        if valor % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False


try:
    assert primo('q') == Exception, f"o valor 'q' não retornou Exception: Saída {repr(primo('q'))}"
    assert primo(3.6) == Exception, f"o valor 3.6 não retornou Exception: Saída {repr(primo('q'))}"
    assert primo({'dic': 5}) == Exception, "o valor {'dic': 5}"\
                                           f" não retornou Exception: Saída {repr(primo({'dic': 5}))}"
    assert primo(-3) == Exception, f"o valor -3 não Retornou Exception: Saída {repr(primo(-3))}"
    assert primo(3) is True, f"o valor 3 não Retornou True: Saída {repr(primo(3))}"
    assert primo(6) is False, f"o valor 6 não Retornou False: Saída {repr(primo(6))}"
    assert primo(27) is False, f"o valor 27 não Retornou False: Saída {repr(primo(27))}"
    print("Teste ok!")
except AssertionError as err:
    print("Ocorreu um erro,", err)
