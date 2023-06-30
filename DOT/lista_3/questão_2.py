"""2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada."""


def media_aluno(nta_1, nta_2, nta_3, ltra):
    # em isinstance() é possível verificar duas ou mais classes, em duas estruturas diferentes:
    # 1 -- isinstance(nta_1, (float, int)) usando tupla
    # 2 -- isinstance(nta_1, float | int) usando essa barra vertical
    if not isinstance(nta_1, (float, int)) or not isinstance(nta_2, (float, int)) \
            or not isinstance(nta_3, (float, int)) or not isinstance(ltra, str):
        return Exception
    elif 0 > nta_1 > 10 and 0 > nta_2 > 10 and 0 > nta_3 > 10:
        return Exception
    elif ltra.upper() != 'A' and ltra.upper() != 'P':
        return Exception

    if ltra.upper() == 'A':
        media = (nta_1 + nta_2 + nta_3) / 3
        return float(f"{media:.2f}")
    elif ltra.upper() == 'P':
        """Para calcular a média ponderada, você precisa multiplicar
         cada nota pelos respectivos pesos e, em seguida, somar esses
          resultados e dividir pela soma dos pesos"""
        peso_n1 = 5 * nta_1
        peso_n2 = 3 * nta_2
        peso_n3 = 2 * nta_3
        total_result = peso_n1 + peso_n2 + peso_n3
        media = total_result / (5 + 3 + 2)

        return float(f"{media:.2f}")


# o método repr() está sendo usado para verificar erros de retorno con str. Isso porque quando retornamos uma str no
# print não é possivel saber se é uma string ou não, o print elimina as aspas da str
try:
    assert media_aluno('34', 45, 6, 'j') == Exception, f"na aplicação dos valores '34', 45, 6, 'j'. Retornou " \
                                                       f"{repr(media_aluno('34', 45, 6, 'j'))}"
    assert media_aluno(12, 45, 'f', 'a') == Exception, f"na aplicação dos valores 12, 45, 'f', 'a'. Retornou " \
                                                       f"{repr(media_aluno(12, 45, 'f', 'a'))}"
    assert media_aluno(12, 45, 67, 'jk') == Exception, f"na aplicação dos valores 12, 45, 67, 'jk' Retornou " \
                                                       f"{repr(media_aluno(12, 45, 67, 'jk'))}"
    assert media_aluno(1.2, 4.5, 9.7, 'jk') == Exception, f"na aplicação dos valores 1.2, 4.5, 9.7, 'jk' Retornou " \
                                                          f"{repr(media_aluno(1.2, 4.5, 9.7, 'jk'))}"
    # anteriormente a função tava retornando o valor numérico correto, porém o tipo era str e o print não mostrava o
    # retorno '4.67' e sim 4.67 dificultando o encontro do erro no assert da função
    assert media_aluno(1, 4, 9, 'A') == 4.67, f"na aplicação dos valores 1, 4, 9, 'A' Retornou " \
                                              f"{repr(media_aluno(1, 4, 9, 'A'))}"
    assert media_aluno(1.2, 4.5, 9.7, 'A') == 5.13, f"na aplicação dos valores 1.2, 4.5, 9.7, 'A' Retornou " \
                                                    f"{repr(media_aluno(1.2, 4.5, 9.7, 'A'))}"
    assert media_aluno(4.7, 7.8, 10, 'P') == 6.69, f"na aplicação dos valores 4.7, 7.8, 10, 'P' Retornou " \
                                                   f"{repr(media_aluno(4.7, 7.8, 10, 'P'))}"
    print("Testes ok!")
except AssertionError as err:
    print("Ocorreu um erro", err)
