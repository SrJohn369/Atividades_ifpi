"""4. Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos."""


def convert_sec(sec: int):
    """A função receberá por parâmetro segundos e retornará
    horas, minutos e segundos no formato -> 00:00:00 """
    if not isinstance(sec, int):
        return Exception
    #   Passo 1: Dividindo por 3600 para encontrar o número de horas:
    #   Divida o número total de segundos pelo número de segundos em uma hora, que é 3600
    horas = sec // 3600
    #   Passo 2: Encontrando o restante dos segundos:
    rest_sec = sec - (horas * 3600)
    #   Passo 3: Dividindo por 60 para encontrar o número de minutos:
    minut = rest_sec // 60
    #   Passo 4: Encontrando o restante dos segundos:
    final_sec = rest_sec - (minut * 60)
    return f"{'0'+str(horas) if horas<10 else str(horas)}:{'0'+str(minut) if minut<10 else str(minut)}:" \
           f"{'0'+str(final_sec) if final_sec<10 else str(final_sec)}"


try:
    assert convert_sec(3.4) == Exception, f"teste com valor 3.4 -> Saída: {repr(convert_sec(3.4))}"
    assert convert_sec('3.4') == Exception, f"teste com valor '3.4' -> Saída: {repr(convert_sec(3.4))}"
    assert convert_sec(300) == "00:05:00",  f"teste com valor 300 -> Saída: {repr(convert_sec(300))}"
    assert convert_sec(10000) == "02:46:40", f"teste com valor 10000 -> Saída: {repr(convert_sec(10000))}"
    assert convert_sec(30000) == "08:20:00", f"teste com valor 30000 -> Saída: {repr(convert_sec(30000))}"
    print("Testes Ok!")
except AssertionError as err:
    print("Ocorreu um erro no", err)

