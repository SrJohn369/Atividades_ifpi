"""1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R**3)."""


def cal_volume(raio):
    if not isinstance(raio, float) and not isinstance(raio, int):
        return Exception

    volume = 4 / 3 * 3.14 * raio ** 3
    return float(f"{volume:.2f}")


try:
    assert cal_volume("Assert") == Exception, "A string 'Assert' não retornou Exception"
    assert cal_volume({"Assert": 5}) == Exception, "O dicionário não retornou Exception"
    assert cal_volume(["Assert", 89]) == Exception, "A lista não retornou Exception"
    assert cal_volume(2) == 33.49, f"usando inteiro 2, o retorno foi {cal_volume(2)}"
    assert cal_volume(1) == 4.19, f"usando inteiro 1 o retorno foi {cal_volume(1)}"
    assert cal_volume(1.6) == 17.15, f"usando float 1.6 o retorno foi {cal_volume(1.6)}"
    assert cal_volume(45.8990) == 404835.0, f"usando float 45.8990 o retorno foi {cal_volume(45.8990)}"
    print("Testes ok!")
except AssertionError as err:
    print("Ocorreu um erro", err)
