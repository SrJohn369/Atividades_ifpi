"""
Alunos: João Victor de Sousa & Maria Eduarda Amarante & Carla Regiane
"""


class Cliente:
    def __init__(self, cpf: str, nome: str, idade: int):
        if isinstance(cpf, str) \
                and isinstance(nome, str) \
                and isinstance(idade, int):
            self.__CL_cpf = cpf
            self.__CL_nome = nome
            self.__CL_idade = idade
        else:
            raise ValueError("Erro ao Iniciar classe Cliente um dos atributos tem valor incorreto")

    @property
    def idade(self) -> int:
        return self.__CL_idade

    @property
    def nome(self) -> str:
        return self.__CL_nome


# ---------------------------------------------------------------------------------------------------------------------#
class Seguro:
    def __init__(self, num_apolice: int, proprietario: Cliente):
        if isinstance(num_apolice, int) and isinstance(proprietario, Cliente):
            self._S_num_apolice = num_apolice
            self._S_proprietario = proprietario
        else:
            raise ValueError("Erro ao Iniciar classe Seguro um dos atributos tem valor incorreto")

    def calcularValor(self):
        pass

    def calcularPremio(self):
        pass

    def __str__(self):
        pass


# ---------------------------------------------------------------------------------------------------------------------#
class SeguroVida(Seguro):
    def __init__(self, num_apolice: int, proprietario: Cliente, nome_beneficiario: str):
        if isinstance(num_apolice, int) \
                and isinstance(proprietario, Cliente) \
                and isinstance(nome_beneficiario, str):
            super().__init__(num_apolice, proprietario)
            self.__SV_nome_bneficiario = nome_beneficiario
        else:
            raise ValueError("Erro ao Iniciar classe SeguroVida um dos atributos tem valor incorreto")

    def calcularValor(self):
        if 18 <= self._S_proprietario.idade < 30:
            return 800
        elif 31 < self._S_proprietario.idade <= 50:
            return 1_300
        elif 50 < self._S_proprietario.idade:
            return 1_600

    def calcularPremio(self):
        if self.calcularValor() == 800:
            return 50_000
        elif self.calcularValor() == 1_300:
            return 30_000
        elif self.calcularValor() == 1_600:
            return 20_000

    @property
    def nomeBeneficiario(self):
        return self.__SV_nome_bneficiario

    def __str__(self):
        return f"""  {"|" + 17 * "=" + " Seguro de Vida " + 23 * "=" + "|"}
  |        Numero da Apolice:   {self._S_num_apolice}
  |        Segurado:            {self._S_proprietario.nome}
  |        Valor:               {self.calcularValor()}
  |        Prêmio:              {self.calcularPremio()}"""


# ---------------------------------------------------------------------------------------------------------------------#
class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice: int, proprietario: Cliente, numero_licenca: int, nome_modelo: str,
                 ano: int, valor_automovel: float):
        if isinstance(num_apolice, int) \
                and isinstance(proprietario, Cliente) and isinstance(num_apolice, int) \
                and isinstance(numero_licenca, int) and isinstance(nome_modelo, str) \
                and isinstance(ano, int) and isinstance(valor_automovel, float):
            super().__init__(num_apolice, proprietario)
            self.__SA_numero_licenca = numero_licenca
            self.__SA_nome_modelo = nome_modelo
            self.__SA_ano = ano
            self.__SA_valor_automovel = valor_automovel
        else:
            raise ValueError("Erro ao Iniciar classe SeguroAutomovel um dos atributos tem valor incorreto")

    def calcularValor(self):
        return (3 / 100) * self.__SA_valor_automovel

    def calcularPremio(self):
        return (80 / 100) * self.__SA_valor_automovel

    def calcularFranquia(self):
        return (40 / 100) * self.calcularValor()

    def __str__(self):
        return f"""  {"|" + 17 * "=" + " Seguro de Automóvel " + 18 * "=" + "|"}
  |     Numero da Apolice:   {self._S_num_apolice}
  |     Segurado:            {self._S_proprietario.nome}
  |     Valor:               {self.calcularValor()}
  |     Prêmio:              {self.calcularPremio()}"""


# ---------------------------------------------------------------------------------------------------------------------#
class ControleDeSeguros:
    def __init__(self):
        self.__CDS_lista_seguros = []

    def cadastrarSeguro(self, seguro_: Seguro):
        self.__CDS_lista_seguros.append(seguro_)

    def inprimirRelatorio(self):
        SV = SA = valor_total = premio_total = 0
        print(10 * "==" + " Relatório de Seguros " + 10 * "==")
        for sg in self.__CDS_lista_seguros:
            print(sg)
            valor_total += sg.calcularValor()
            premio_total += sg.calcularPremio()
            if isinstance(sg, SeguroVida):
                SV += 1
            elif isinstance(sg, SeguroAutomovel):
                SA += 1
        print(62 * "=")
        print(
            f"\t\t\tSeguros de vida:        {SV}\n"
            f"\t\t\tSeguros de Automoveis:  {SA}\n"
            f"\t\t\tValor total:            {valor_total}\n"
            f"\t\t\tPremio Total:           {premio_total}"
        )


# ---------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    # Criando Instâncias
    clientes = [
        Cliente("12345678901", "João", 25),
        Cliente("98765432109", "Maria", 32),
        Cliente("45678912345", "Pedro", 18),
        Cliente("78901234567", "Ana", 40),
        Cliente("23456789012", "Lucas", 21),
        Cliente("45346456762", "Roberta", 27)
    ]
    # Criando uma Lista de instancias De Seguros para adicionar em Controle
    seguros = [
        SeguroAutomovel(12345, clientes[0], 123, "Modelo 1", 2022, 10000.0),
        SeguroAutomovel(2, clientes[1], 456, "Modelo 2", 2021, 15000.0),
        SeguroVida(3, clientes[0], clientes[0].nome),
        SeguroVida(4, clientes[1], clientes[1].nome),
        SeguroAutomovel(5, clientes[2], 789, "Modelo 3", 2023, 20000.0),
        SeguroAutomovel(6, clientes[4], 101112, "Modelo 4", 2020, 18000.0),
        SeguroVida(7, clientes[2], clientes[2].nome),
        SeguroVida(8, clientes[4], clientes[4].nome),
        SeguroAutomovel(9, clientes[3], 131415, "Modelo 5", 2022, 25000.0),
        SeguroAutomovel(10, clientes[5], 161718, "Modelo 6", 2023, 22000.0)
    ]

    # Criando uma instância para adicionar Seguros
    controle = ControleDeSeguros()
    # Cadastrando Seguros no Controe
    for seguro in seguros:
        controle.cadastrarSeguro(seguro)
    # Imprimindo Relatório
    controle.inprimirRelatorio()
