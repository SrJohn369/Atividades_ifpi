"""
Alunos: João Victor de Sousa & Andressa Felix Almeida Nascimento
"""
from datetime import date


class CartaoDeCredito:
    __data_atual_ano = date.today().year
    __data_atual_mes = date.today().month

    def __init__(self, numero, titular, validade: tuple, cod_seguranca,
                 senha=None, fatura_a_pagar=0,
                 status='bloqueado', limite_de_compras=1000):
        self.__numero = numero
        self.__validade = validade
        self.__limite_de_compras = limite_de_compras
        self.__cod_seguranca = cod_seguranca
        self.__fatura_a_pagar = fatura_a_pagar
        self.__valor_minimo_a_pagar = 0
        self.__status = status
        self.__titular = titular
        self.__senha = senha

    @property
    def numero(self):  # Não tem setter
        return self.__numero

    @property
    def validade(self):  # Não tem setter
        return self.__validade

    @property
    def limite_de_compras(self):  # Não tem setter
        return self.__limite_de_compras

    @property
    def cod_seguranca(self):  # Não tem setter
        return self.__cod_seguranca

    @property
    def fatura_a_pagar(self):  # Não tem setter
        return self.__fatura_a_pagar

    @property
    def valor_minimo_a_pagar(self):  # Não tem setter
        return self.__valor_minimo_a_pagar

    @property
    def status(self):  # Não tem setter
        return self.__status

    @property
    def senha(self):  # Não tem setter
        return self.__senha

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        if self.__titular == '':
            self.__titular = valor
        else:
            print('Não permitido, o cartão já possui um titular')

    def __str__(self):
        return f"\tNúmero do Cartão:\t\t{self.__numero}\n" \
               f"\tNome do Titular:\t\t{self.__titular}\n" \
               f"\tValor da Fatura:\t\tR${self.__fatura_a_pagar:.2f}\n" \
               f"\tValor Mínimo a Pagar:\tR${self.__valor_minimo_a_pagar:.2f}"

    def desbloquear(self):
        if self.__titular != "" and self.__senha is not None:
            if self.__validade[0] >= self.__data_atual_ano or \
                    self.__validade[1] >= self.__data_atual_mes:
                if self.__status == 'bloqueado':
                    self.__status = 'liberado'
                    return 'Cartão liberado!'
                elif self.__status == 'liberado':
                    return f'Cartão já está liberado!'
            else:
                return 'Não foi possível desbloquear cartão vencido!'
        else:
            return 'Não foi possível desbloquear cartão, senha ou titular não fornecidos'

    def bloquear(self):
        if self.__status == 'bloqueado':
            return 'Cartão já está bloqueado!'
        elif self.__status == 'liberado':
            self.__status = 'bloqueado'
            return f'Cartão foi bloqueado!'

    def mudar_senha(self, num_cartao, cod_seguranca, nova_senha):
        if num_cartao == self.__numero:

            if cod_seguranca == self.__cod_seguranca:
                self.__senha = nova_senha
                return 'Senha alterada com sucesso!'
            elif cod_seguranca != self.__cod_seguranca:
                return 'Código de segurança inválido!'

        else:
            return 'Número de cartão inválido!'

    def comprar(self, valor_compra, senha):
        if valor_compra < 0:
            return 'Valor de compra inválido'
        if valor_compra <= self.__limite_de_compras:
            if self.__status == 'bloqueado':
                return 'Compra não realizada! Cartão bloqueado!'
            else:
                if self.__validade[0] >= self.__data_atual_ano or \
                        self.__validade[1] >= self.__data_atual_mes:
                    if self.__senha is not None:
                        if self.__senha == senha:
                            self.__limite_de_compras -= valor_compra
                            self.__fatura_a_pagar += valor_compra
                            self.__valor_minimo_a_pagar = self.fatura_a_pagar * 0.3
                            return 'Compra realizada com sucesso!'
                        else:
                            return 'Compra não realizada. Senha inválida!'
                    else:
                        return 'Cartão não foi definida'
                else:
                    return 'Compra não realizada, cartão vencido!'
        else:
            return 'Compra não realizada. Cartão rejeitado! ' \
                   'Valor acima do limite!'

    def pagar_fatura(self, valor_a_pagar):
        if self.__valor_minimo_a_pagar <= valor_a_pagar <= self.__fatura_a_pagar:
            self.__fatura_a_pagar -= valor_a_pagar
            self.__limite_de_compras += valor_a_pagar
            return f'Fatura paga! Falta R$ {self.__fatura_a_pagar:.2f} a pagar'
        else:
            return f'O valor de R$ {valor_a_pagar:.2f} é insifuciente para pagar o valor mínimo de ' \
                   f'R$ {self.__valor_minimo_a_pagar:.2f} ou ultrapassa o valor da fatura R$ {self.__fatura_a_pagar:.2f}'


# # # EXECUÇÃO # # #
# # # OBS: Foi usado return nas funções por causa do método comprar() na verificaçõa
#       if valor_compra < 0:
#             return 'Valor de compra inválido'
# a fim de finalizar a função se a verificação for verdadeira
cartoes = [
    CartaoDeCredito(12345, 'Manoel Gomes', (2002, 3), 456, senha=5678),
    CartaoDeCredito(34556, 'Andressa Felix', (2026, 9), 789),
    CartaoDeCredito(34567, 'Carla Lima', (2023, 2), 719, senha=8970),
    CartaoDeCredito(34569, 'João Victor', (2027, 3), 769, senha=4321, status='liberado', limite_de_compras=2000),
    CartaoDeCredito(43212, '', (2029, 9), 432)
]

#  ---Manoel Gomes---  #
print(cartoes[0].titular)
cartoes[0].titular = 'Raimundo'
print(cartoes[0].comprar(345.67, 5678))
print(cartoes[0].desbloquear())
print(cartoes[0].comprar(345.67, 5678))
print('Dados do cartão:')
print(cartoes[0])
print()
#  ---Andressa Felix---  #
print(cartoes[1].titular)
print(cartoes[1].comprar(345.67, 567348))
print(cartoes[1].desbloquear())
print(cartoes[1].comprar(345.67, 56745))
print(cartoes[1].mudar_senha(34556, 786, 5678))
print(cartoes[1].mudar_senha(34556, 789, 5678))
print(cartoes[1].comprar(345.67, 56745))
print(cartoes[1].comprar(345.67, 5678))
print('Dados do cartão:')
print(cartoes[1])
print()
#  ---Carla Lima---  #
print(cartoes[2].titular)
cartoes[2].titular = 'Raimundo'
print(cartoes[2].comprar(345.67, 567348))
print(cartoes[2].desbloquear())
print(cartoes[2].comprar(345.67, 56745))
print(cartoes[2].mudar_senha(34556, 786, 5678))
print(cartoes[2].mudar_senha(34556, 789, 5678))
print(cartoes[2].comprar(345.67, 56745))
print(cartoes[2].comprar(345.67, 5678))
print('Dados do cartão:')
print(cartoes[2])
print()
#  ---João Victor---  #
print(cartoes[3].titular)
cartoes[3].titular = 'Raimundo'
print(cartoes[2].desbloquear())
print(cartoes[3].comprar(345.67, 4321))
print('Dados do cartão:')
print(cartoes[3])
print()
#  ---''---  #
print(cartoes[4].titular)
cartoes[4].titular = 'Rogério Silva'
print(cartoes[4].titular)
print(cartoes[4].desbloquear())
print(cartoes[4].mudar_senha(43212, 432, 6779))
print(cartoes[4].comprar(345.67, 4321))
print(cartoes[4].desbloquear())
print(cartoes[4].comprar(345.67, 4321))
print(cartoes[4].comprar(345.67, 6779))
print('Dados do cartão:')
print(cartoes[4])
print()
