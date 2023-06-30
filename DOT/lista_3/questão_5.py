"""Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias."""


def idade_dias(ano, mes, dia):
    if not isinstance(ano, int) or not isinstance(mes, int) or not isinstance(dia, int):
        return Exception
    if mes > 12 or mes <= 0:
        return Exception


try:
    assert idade_dias(34.77, 54.23, 65.34) == Exception, f"teste com valor 34.77, 54.23, 65.34" \
                                                         f" -> Saída: {repr(idade_dias(34.77, 54.23, 65.34))}"
    assert idade_dias(34.77, 54.23, 65) == Exception, f"teste com valor 34.77, 54.23, 65" \
                                                      f" -> Saída: {repr(idade_dias(34.77, 54.23, 65))}"
    assert idade_dias(34.77, 54, 65) == Exception, f"teste com valor 34.77, 54, 65" \
                                                   f" -> Saída: {repr(idade_dias(34.77, 54, 65))}"
    assert idade_dias(34, 54, 65) == Exception, f"teste com valor 34, 54, 65" \
                                                f" -> Saída: {repr(idade_dias(34, 54, 65))}"
    print("Teste Ok!")
except AssertionError as err:
    print("Ocorreu um erro no", err)
