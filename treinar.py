# altura = float(input('Digite a altura:'))
# raio = float(input('Digite o raio:'))
# pi = 3.14
# Área_lateral = 2*pi*raio*altura
# print('A área lateral do cilindro é:',Área_lateral)

# valor1 = float(input('Digite um valor:'))
# valor2 = float(input('Digite um valor:'))
# if valor1 > valor2:
#     print('A ordem crescente dos valores é:',valor2,valor1)
# if valor2 > valor1:
#     print('A ordem crescente dos valores é:',valor1,valor2)

ct = 0
soma = 0
while True:
    valor = float(input('Digite um valor:'))
    if valor == 0:
        break
    if valor != 0:
        ct = ct + 1
        soma = soma + valor
        Média_Aritmética = soma/ct
    print('A quantidade de valores digitados foi:',ct)
    print('A soma dos valores digitados é:',soma)
    print('A média aritmética dos valores é:',Média_Aritmética)



