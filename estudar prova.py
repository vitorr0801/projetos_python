# numero = int(input('Digite um núumero inteiro positivo:'))
# for i in range(0,numero+1):
#     if i%2 == 0:
#         print(i)
# numero = int(input('Digite um número positivo:'))
# soma_impar = 0
# for i in range(1,numero+1):
#     if i %2 == 1:
#         soma_impar = soma_impar + i
#         print(i)
# print('A soma dos números exibidos é:',soma_impar)
# soma = 0
# for i in range(1,10+1):
#     soma = soma + i*2
# print(f'{i*2}A soma dos valores é: {soma}')
# n = int(input('Digite um número:'))
# soma = 0
# for i in range(0,n+1):
#     soma = soma + i
#     print(i)
# print(f'a soma destes números exibidos é:{soma}')
#
# produto = 1
# for i in range(10):
#     numero = int(input('Digite um número:'))
#     produto = produto * numero
# print('O produto dos números é:',produto)

# print('Digite [-1] para sair')
# l_numeros = list()
# while True:
#     numero = int(input('Digite um número:'))
#     if numero == -1:
#         break
#     l_numeros.append(numero)
#     print(l_numeros)
# qtd_numeros = len(l_numeros)
# soma_numeros = sum(l_numeros)
# maior_numero = max(l_numeros)
# menor_numero = min(l_numeros)
# print('A quantidade de números digitados foi:',qtd_numeros)
# print('A soma dos números digitados é:',soma_numeros)
# print('O maior número digitado foi:',maior_numero)
# print('O menor número digitado foi:',menor_numero)

l_tarefas = list()
print('Bem vindo ao programa de lista de tarefas!')
while True:
    print('1- Adicionar tarefa à lista\n2- Exibir a lista de tarefas\n3- Finalizar o programa')
    opções = int(input('Digite o número da opção que deseja:'))
    if opções == 1:
        tarefa = str(input('Escreva uma tarefa a fazer:'))
        l_tarefas.append(tarefa)
    if opções == 2:
        print('Tarefas na lista:',l_tarefas)
    if opções == 3:
        print('Programa finalizado')
        break





















