class Cliente:
    def __init__(self, pais, dataCadastro):
        self.Cl_pais = pais
        self.Cl_dataCadastro = dataCadastro


class PessoaFisica(Cliente):  # Definição de Herença, Classe PessoaFisica herda Todos os atributos e metodos da Cliente
    def __init__(self, pais, dataCadastro, nome, sobrenome, cpf):
        super().__init__(pais, dataCadastro)
        self.PF_nome = nome
        self.PF_sobrenome = sobrenome
        self.PF_cpf = cpf


class PessoaJuridica(Cliente):
    # Definição de Herença, Classe PessoaJuridica herda Todos os atributos e metodos da Cliente
    def __init__(self, pais, dataCadastro, razaoSocial, nomeFantazia, cnpj):
        super().__init__(pais, dataCadastro)
        self.PJ_razaoSocial = razaoSocial
        self.PJ_nomeFantazia = nomeFantazia
        self.PJ_cnpj = cnpj


# Instancias test
IPF_Maria = PessoaFisica("Brasil", "29/02/1999", "Maria", "Perreira", "4567890633")
IPJ_Google = PessoaJuridica("US", "24/12/2000", "Google", "Google", "12345678909876543")

print(IPF_Maria.Cl_pais)
print(IPF_Maria.Cl_dataCadastro)
print(IPJ_Google.Cl_pais)
print(IPJ_Google.PJ_razaoSocial)
