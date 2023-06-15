from time import sleep


class Bateria:
    __carg_atual = 0
    __porcent_carg = 0

    def __init__(self, cod_bat: int, cap_MAh: float):
        self.__cod_bat = cod_bat
        self.__cap_MAh = cap_MAh

    @property
    def cod_bat(self):
        return self.__cod_bat

    @property
    def cap_MAh(self):
        return self.__cap_MAh

    @property
    def porcent_carg(self):
        return self.__porcent_carg

    def __str__(self):
        return f'Código da bateria:\t{self.cod_bat}\n' \
               f'Capacidade MAh:\t\t{self.cap_MAh}\n' \
               f'Porcentagem:\t\t{self.porcent_carg}'

    def __calcula_porcent(self):
        self.__porcent_carg = (self.__carg_atual * 100) / self.cap_MAh

    def carregar(self, valor):
        if 30 <= valor <= 100:
            if self.__porcent_carg <= 15:
                equivalente = (self.__cap_MAh * valor) / 100
                self.__carg_atual = equivalente
                self.__calcula_porcent()
                return f'Bateria carregada {self.porcent_carg:.0f}%'
            elif self.__porcent_carg <= 31:
                return 'É recomendável que carregue a bateria com no máximo 30%'
            elif self.__porcent_carg == 100:
                return 'A bateria já está carregada!'
        elif valor < 30:
            return 'É recomendado que seja carregada com no mínimo 30%'
        elif valor > 100:
            return 'Não é possível carregar a bateria com mais de 100%'

    def descarregar(self, valor):
        self.__carg_atual -= valor
        self.__calcula_porcent()


class Celular:
    __wifi: bool

    def __init__(self, bateria: object, mei: int):
        self.__bateria = bateria
        self.__mei = mei

    @property
    def bateria(self):
        return self.__bateria

    @property
    def mei(self):
        return self.__mei

    @property
    def wifi(self):
        return self.__wifi

    def ligarDesligar(self):
        pass

    def colocarBateria(self):
        pass

    def ligDeslWifi(self):
        pass

    def assistVideo(self):
        pass

    def carregarCell(self):
        pass

    def __descarregar(self):
        pass