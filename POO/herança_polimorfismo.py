class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__F_nome = nome
        self._F_cpf = cpf
        self._F_salario = salario

    def get_bonificacao(self):
        return self._F_salario * 0.10

    @property
    def nome(self):
        return self.__F_nome


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, tamanho):
        super().__init__(nome, cpf, salario)
        self.__FG_senha = senha
        self.tamanhoEquipe = tamanho

    def get_bonificacao(self):
        return self._F_salario * 0.15


joao = Funcionario("Joao", "12344325436", 1500)
jose = Gerente("Jose", "435435", 3000, '21234', 20)

print(f"A bonificação de {joao.nome} é {joao.get_bonificacao()}")
print(f"A bonificação de {jose.nome} é {jose.get_bonificacao()}")

