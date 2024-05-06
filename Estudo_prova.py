# class Veiculo(object):
#     def __init__(self, marca, modelo, ano, preco):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.preco = preco
#     def get_marca(self):
#         return self.marca
#     def set_marca(self, nova_marca):
#         self.marca = nova_marca
#     def get_modelo(self):
#         return self.modelo
#     def set_modelo(self, novo_modelo):
#         self.modelo = novo_modelo
#     def get_ano(self):
#         return self.ano
#     def set_ano(self, novo_ano):
#         self.ano = novo_ano
#     def get_preco(self):
#         return self.preco
#     def set_preco(self, preco):
#         if preco > 0:
#             self.preco = preco
#         else:
#             print("O preço do carro não pode ser negativo")
#     def exibir_info(self):
#         print(f"Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}, Preço:{self.preco}")
# class Carro(Veiculo):
#     def __init__(self, marca='', modelo='', ano=0, preco=0, qtd_portas=0 ):
#         super().__init__(modelo, marca, ano, preco)
#         self.qtd_portas = qtd_portas
#     def get_qtd_portas(self):
#         return self.qtd_portas
#     def exibir_info(self):
#         super().exibir_info()
#         print(f"Quantidade de portas:{self.qtd_portas}")
# class Moto(Veiculo):
#     def __init__(self, marca='', modelo='', ano=0, preco=0, cilindradas=0 ):
#         super().__init__(modelo, marca, ano, preco)
#         self.cilindradas = cilindradas
#     def get_cilindradas(self):
#         return self.cilindradas
#     def exibir_info(self):
#         super().exibir_info()
#         print(f"Cilindradas: {self.cilindradas}")
# if __name__ == '__main__':
#     V = Veiculo("Honda", "Civic", 2021, 120000.00)
#     print(V)
#     V.exibir_info()
#     C = Carro("Porsche", "Panamera", 2024, 1000000.00, 4)
#     print(C)
#     C.exibir_info()
#     M = Moto("Honda", "cb500", 2020, 20000.00, 500)
#     print(M)
#     M.exibir_info()

# from abc import ABC, abstractmethod
# import math
# class Figura(ABC):
#     @abstractmethod
#     def calcula_area(self):
#         """Calcula a área da figura"""
#         pass
#
#     @abstractmethod
#     def calcula_perimetro(self):
#         """Calcula o perimetro da figura"""
#         pass
# class Circulo(Figura):
#     def __init__(self, raio):
#         self.raio = raio
#
#     def calcula_area(self):
#         return math.pi * self.raio ** 2
#
#     def calcula_perimetro(self):
#         return 2 * math.pi * self.raio
# class Retangulo(Figura):
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
#
#     def calcula_area(self):
#         return  self.largura * self.altura
#
#     def calcula_perimetro(self):
#         return 2*(self.largura + self.altura)
# if __name__ == '__main__':
#     Circulo1 = Circulo(7)
#     print(f"Área do círculo: {Circulo1.calcula_area()}")
#     print(f"Perímetro o círculo`: {Circulo1.calcula_perimetro()}")
#     Retangulo1 = Retangulo(4, 10)
#     print(f"Área do retângulo: {Retangulo1.calcula_area()}")
#     print(f"Perímetro do retângulo:{Retangulo1.calcula_perimetro()}")

from abc import ABC, abstractmethod
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        """"Processa o pagamento conforme o tipo."""
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor):
        self.valor = valor

    def processar_pagamento(self):
        return print(f"O pagamento de R${self.valor:.2f}  foi processado via cartão de crédito.")

class Paypal(Pagamento):
    def __init__(self, valor):
        self.valor = valor

    def processar_pagamento(self):
        return print(f"O pagamento de R${self.valor:.2f} foi processado via paypal.")

class TransferenciaBancaria(Pagamento):
    def __init__(self, valor):
        self.valor = valor

    def processar_pagamento(self):
        return print(f"O pagamento de R${self.valor:.2f} foi processado via transferência bancária.")

if __name__ == '__main__':
    cartao1 = CartaoCredito(200)
    print(cartao1)
    cartao1.processar_pagamento()
    paypal1 = Paypal(1000)
    print(paypal1)
    paypal1.processar_pagamento()
    transferencia1 = TransferenciaBancaria(345.90)
    print(transferencia1)
    transferencia1.processar_pagamento()



