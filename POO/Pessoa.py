class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float,
                 sexo: str, estado: str = 'vivo', conjuge: str = 'Não consta', estado_civil: str = "Solteiro(a)"):
        self.__nome = nome
        self.__idade = idade
        self._peso = peso
        self._altura = altura
        self._sexo = sexo
        self.__estado = estado
        self.__conjuge = conjuge
        self._estado_civil = estado_civil

    def __str__(self):
        return f'Nome:\t{self.__nome}\n' \
               f'Idade:\t{self.__idade}\n' \
               f'Peso:\t{self._peso}\n' \
               f'Altura:\t{self._altura}\n' \
               f'Sexo:\t{self._sexo}\n' \
               f'Estado de vida:\t{self.__estado}\n' \
               f'Conjuge:\t{self.__conjuge}\n' \
               f'Estado civil:\t{self._estado_civil}\n'

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if self.__idade >= 100 > idade:
            self.__idade = idade
        else:
            print('Sem permissão')

    @property
    def estado(self):
        return self.__estado

    @property
    def conjuge(self):
        return self.__conjuge

    def envelhecer(self):
        if self.__estado == 'vivo':
            self.__idade += 1
            if self.__idade < 21:
                self._altura += 0.5
            print(f'{self.__nome} está com {self.__idade} anos e com {self._altura}cm de altura.')

        elif self.estado == 'morto':
            print(f'{self.__nome} está morto(a)')

    def engordar(self, quilos):
        if self.__estado == 'vivo':
            self._peso += quilos

        elif self.estado == 'morto':
            print(f'Operação não realizada. {self.__nome} está morto(a)!')

    def emagrecer(self, quilos):
        if self.__estado == 'vivo':
            self._peso -= quilos

        elif self.estado == 'morto':
            print(f'{self.__nome} está morto(a)')

    def crescer(self, cm):
        if self.__estado == 'vivo':
            if self.__idade < 21:
                self._altura += cm

            else:
                print(f'{self.__nome} não pode crescer mais pois está com 21 anos ou mais')

        elif self.estado == 'morto':
            print(f'{self.__nome} está morto(a)')

    def casar(self, nome_conjude: str, idade_conjude: int):
        if self.__estado == 'vivo':
            if not self._estado_civil == 'Casado(a)':
                if self.__conjuge == 'Não consta':
                    if not self.__idade < 18:
                        if not idade_conjude < 18:
                            self._estado_civil = 'Casado(a)'
                            self.__conjuge = nome_conjude
                            print(f'{self.__nome} está casdo com {self.__conjuge}')

                        else:
                            print(f'Casameno não permitido. {nome_conjude} é menor de idade')

                    else:
                        print(f'Casameno não permitido. {self.__nome} é menor de idade')

            elif self._estado_civil == 'Casado(a)':
                print(f'Casamento não realizado. {self.__nome} já é casado!')

        elif self.estado == 'morto':
            print(f'{self.__nome} está morto(a)')

    def morrer(self):
        if self.estado == 'vivo':
            self.__estado = 'morto'
            print(f'{self.__nome} morreu')

        elif self.estado == 'morto':
            print(f'{self.__nome} já está morto!')


def main():
    pessoa = [Pessoa('Maria', 5, 20, 100, 'F'), Pessoa('João', 12, 40, 140, 'M'),
              Pessoa('Pedro', 22, 65, 170, 'M'), Pessoa('Bia', 18, 55, 160, 'F'),
              Pessoa('Júlia', 30, 65, 170, 'F'), Pessoa('Carlos', 2, 11, 80, 'M'),
              Pessoa('Jonas', 34, 70, 180, 'M')]

    print('A)')
    pessoa[0].idade = 10
    print('B)')
    pessoa[0].envelhecer()
    print('C)')
    pessoa[2].crescer(2)
    print('D)')
    pessoa[3].casar(pessoa[5].nome, pessoa[5].idade)
    print('E)')
    pessoa[2].casar(pessoa[0].nome, pessoa[0].idade)
    print('F)')
    pessoa[2].casar(pessoa[4].nome, pessoa[4].idade)
    print('G)')
    pessoa[2].casar(pessoa[3].nome, pessoa[3].idade)
    print('H)')
    pessoa[0].morrer()
    print('I)')
    pessoa[0].engordar(4)
    print('J)')
    pessoa[3].casar(pessoa[6].nome, pessoa[6].idade)
    print('K)')
    pessoa[3].morrer()
    print('L)')
    pessoa[2].morrer()
    print('M)')
    pessoa[6].casar(pessoa[4].nome, pessoa[4].idade)
    print('N)')
    pessoa[2].casar(pessoa[3].nome, pessoa[3].idade)
    print('O)')
    print(pessoa[2].idade)
    print('P)')
    pessoa[1].idade = 50


if __name__ == '__main__':
    main()
