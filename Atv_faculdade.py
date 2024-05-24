import mysql.connector

conexao_at = mysql.connector.connect(user="root", password="", host="localhost")
print("Conexão:\n", conexao_at)
cursor = conexao_at.cursor()
sql = "CREATE DATABASE if not exists db_concessionaria"
cursor.execute(sql)
cursor.close()
conexao_at.close()
print("\nConexão fechada.")

import mysql.connector

conexao = mysql.connector.connect(user="root", password="", host="localhost", database="db_concessionaria")
print("Conexão:\n", conexao_at)
cursor = conexao_at.cursor()
sql = ''' CREATE TABLE IF NOT EXISTS tb_carro(
          idt INT NOT NULL AUTO_INCREMENT,
          chassi VARCHAR(17) NOT NULL UNIQUE,
          nome_carro VARCHAR(50) NOT NULL,
          valor_carro DECIMAL(11,2) NULL,
          data_lancamento DATE NULL,
          PRIMARY KEY (idt)
    )'''
cursor.execute(sql)
cursor.close()
conexao.close()
print("\nConexão fechada.")

import mysql.connector

conexao = mysql.connector.connect(user="root", password="", host="localhost", database="db_concessionaria")
print("Conexão:\n", conexao_at)
cursor = conexao_at.cursor()
var_chassi = int(input("Digite o chassi do veículo:"))
var_nome = input("Digite o nome do veículo:")
var_valor = float(input("Digite o valor do carro:"))
var_lancamento = input("Digite a data de lancamento do carro:")
sql = f''' insert into tb_carro
           (chassi, nome_carro, valor_carro, data_lancamento)
           values ('{var_chassi}', '{var_nome}', {var_valor}, '{var_lancamento}')'''
cursor.execute(sql)
conexao.commit()
sql = f''' insert into tb_carro
           (chassi, nome_carro, valor_carro, data_lancamento)
           values ('{var_chassi}', '{var_nome}', {var_valor}, '{var_lancamento}')'''
cursor.execute(sql)
conexao.commit()
sql = f''' insert into tb_carro
           (chassi, nome_carro, valor_carro, data_lancamento)
           values ('{var_chassi}', '{var_nome}', {var_valor}, '{var_lancamento}')
                  ('{var_chassi}', '{var_nome}', {var_valor}, '{var_lancamento}') '''
cursor.execute(sql)
conexao.commit()
print("Registros inseridos com sucesso!")
cursor.close()
conexao_at.close()
print("\nConexão fechada.")

import mysql.connector

conexao_at = mysql.connector.connect(user="root", password="", host="localhost", database="db_concessionaria")
print("Conexão:\n", conexao_at)
cursor = conexao_at.cursor()
sql = "select * from tb_carro"
cursor.execute(sql)
l_registros = cursor.fetchall()
print(l_registros)
for record in l_registros:
    print(record)
for record in l_registros:
    print("ID:", record[0])
    print("Quantidade de registros na tabela(rowcount):", cursor.rowcount)
    print("Quantidade de registros na tabela(len):", len(l_registros))
else:
    print("Tabela vazia.")
cursor.close()
conexao_at.close()
print("\nConexão fechada.")