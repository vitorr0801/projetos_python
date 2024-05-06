# class Aluno:
#     def __init__(self, nome, mensalidade, idade):
#         self.nome = nome
#         self.mensalidade = mensalidade
#         self.idade = idade
#
#     def get_nome(self):
#         return self.nome
#     def set_nome(self,novo_nome):
#         self.nome = novo_nome
#     def get_mensalidade(self):
#         return self.mensalidade
#     def set_mensalidade(self, nova_mensalidade):
#         self.mensalidade = nova_mensalidade
#     def get_idade(self):
#         return self.idade
#     def set_idade(self, nova_idade):
#         self.idade = nova_idade
#     def mostra_dados(self):
#         print("Nome:", self.nome)
#         print("Mensalidade:", self.mensalidade)
#         print("Idade:", self.idade)
#     def retorna_daods(self):
#         dados = f'{self.get_nome()}, {self.get_mensalidade()}, {self.get_idade()}'
#         return dados
#     def aumentar_mensalidade(self, aumento):
#         self.mensalidade += aumento
# if __name__ == '__main__':
#     aluno1 = Aluno("Jorge", 1150.00, 20)
#     print(aluno1)
#     aluno2 = Aluno("Marcelo", 2200.50, 19)
#     print(aluno2)
#     print("Aluno1:")
#     print("-Nome:", aluno1.get_nome())
#     print("-Mensalidade:", aluno1.get_mensalidade())
#     print("-Idade:", aluno1.get_idade())
#     print("Aluno2:")
#     print("-Nome:", aluno2.get_nome())
#     aluno1.set_nome("Ronaldo")
#     print("Nome atualizado do aluno1:", aluno1.get_nome())
#     aluno1.mostra_dados()
#     print("Dados concatenados do aluno1:\n", aluno1.retorna_daods())
#     print("Dados concatenados do aluno2:\n", aluno2.retorna_daods())

import datetime
class Pessoa:
    def __init__(self, nome, peso, altura, ano_nascimento):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print("Erro: nome deve ser sttring")
    def get_peso(self):
        return self.peso
    def set_peso(self, novo_peso):
        self.peso = novo_peso
    def get_altura(self):
        return self.altura
    def set_altura(self, nova_altura):
        self.altura = nova_altura
    def get_ano_nascimento(self):
        return self.ano_nascimento
    def set_ano_nascimento(self, novo_ano_nascimento):
        self.ano_nascimento = novo_ano_nascimento
    def imc(self):
        vl_imc = self.peso/(self.altura * self.altura)
        return vl_imc
    def calcula_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.ano_nascimento
        return idade
    def mais_velho(self, obj):
        if self.ano_nascimento < obj.ano_nascimento:
            print(f' A pessoa nascida em {self.ano_nascimento} é mais velha')
        elif obj.ano_nascimento < self.ano_nascimento:
            print(f' A pessoa nascida em {obj.ano_nascimento} é mais velha')
        else:
            print("As duas pessoas nasceram no mesmo ano")
if __name__ == '__main__':
    pessoa1 = Pessoa("kleber", 78, 1.80, 2000)
    print(pessoa1)
    print("Pessoa1:")
    print("-Nome:", pessoa1.get_nome())
    print("-Peso:", pessoa1.get_peso())
    print("-Altura:", pessoa1.get_altura())
    print("-Ano de nascimento:", pessoa1.get_ano_nascimento())
    pessoa2 = Pessoa("Aloísio", 103, 1.82, 1974)
    print("Pessoa2:")
    print("-Nome:", pessoa2.get_nome())
    print("-Peso:", pessoa2.get_peso())
    print("-Altura:", pessoa2.get_altura())
    print("-Ano de nascimento:", pessoa2.get_ano_nascimento())
    pessoa1.set_nome("Tobias")
    pessoa1.set_peso(85)
    print("Dados atualizados da Pessoa1:")
    print("-Nome:", pessoa1.get_nome())
    print("-Peso:", pessoa1.get_peso())
    print("-Altura:", pessoa1.get_altura())
    print("-Ano de nascimento:", pessoa1.get_ano_nascimento())
    print("Idade da pessoa 1:", pessoa1.calcula_idade())
    print("Idade da pessoa 2:", pessoa2.calcula_idade())
    print("IMC da pessoa 1:", pessoa1.imc())
















