import mysql.connector
def create_database():  #cria a base de dados para e chama ela com "create_database()"
    conexao = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    print("Conexao:\n", conexao)
    cursor = conexao.cursor()
    sql = "CREATE DATABASE if not exists db_loja_4"
    cursor.execute(sql)
    cursor.close()
    conexao.close()
    print("\nConexao database fechada.")
def create_connection():       #cria a conexao com a base de dados e chama com "conexao = create_connection()"
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database= 'db_loja_4')
    print('Conexão:', con)
    return con
def close_connection(): #cria a funcao de fechar a base de dados e deve ser
                        #sempre por ultimo no main e chama com "close_connection()"
    conexao.close()
    cursor.close()
    print("\nConexao fechada.")
def create_table():     #cria a tabela
    sql = ''' CREATE TABLE IF NOT EXISTS tb_produto(
              idt INT NOT NULL AUTO_INCREMENT,
              nome_produto VARCHAR(200) NOT NULL UNIQUE,
              preco DECIMAL(9,2) NOT NULL,
              data_validade DATE NULL,
              PRIMARY KEY (idt)
        )'''
    cursor.execute(sql)
def insert_database():  #insere um input para adicionar dados na tabela
    var_produto = input("Digite o nome do produto:")
    var_preco = float(input("Digite o preço do produto:"))
    var_validade = input("Digite a data de validade do produto:")
    sql = f''' insert into tb_produto   
                (nome_produto, preco, data_validade)
                values ('{var_produto}', {var_preco}, '{var_validade}') '''
    cursor.execute(sql)
    conexao.commit()  #atualiza os registros no banco
def select_database():
    sql = " select * from tb_produto "
    cursor.execute(sql)
    l_registros = cursor.fetchall()  #fetchall pega os resultados e joga numa lista
    for record in l_registros:  #mostra na vertical
        print(record)
    print(l_registros)   #mostra na horizontal
    print("-Colunas, notaçao do vetor:")
    for record in l_registros:  #mostrar na vertical mais limpo
        print("-Idt:", record[0])
        print("-Nome:", record[1])
        print("-Preço:", record[2])
        print("-Data de validade:", record[3])
if __name__ == '__main__':
    create_database()   #cria a base de dados
    conexao = create_connection()   #chama o create e cria a conexão
    cursor= conexao.cursor()  #cria o cursor
    create_table()      #cria a tabela
    insert_database()   #insere dados na tabela
    insert_database()   #insere dados na tabela
    select_database()   #chama o select, consulta os registros
    close_connection()  #fecha a conexao
