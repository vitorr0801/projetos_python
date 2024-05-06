numero = float(input('Digite o 1o número:'))
numero1 = float(input('Digite o 2o número:'))
numero2 = float(input('Digite o 3o número:'))
def ler_numeros(numero,numero1,numero2):
    print(f'Os números lidos são: {numero},{numero1} e {numero2}')
ler_numeros(numero,numero1,numero2)
def calcular_soma(numero,numero1,numero2):
    return numero+numero1+numero2
resultado = numero+numero1+numero2
print(f'A soma é: {resultado}')
def calcular_media(numero,numero1,numero2):
    return (numero+numero1+numero2)/3
resultado = (numero+numero1+numero2)/3
print(f'A média é: {resultado}')


