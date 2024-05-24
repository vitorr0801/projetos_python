import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user= 'root',password='',host='127.0.0.1')
    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE if not exists db_cadastro"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\n Conexão db fechada.')
def create_connection():
    con = mysql.connector.connect(user= 'root',password='',host='127.0.0.1', database = 'db_cadastro')
    print('Conexão:', con)
    return con
def close_connection():
    cursor.close()
    conexao.close()
    print("\n Conexão fechada.")
def create_table():     #cria a tabela
    sql_cargo = ''' CREATE TABLE IF NOT EXISTS td_cargo(
              idt INT NOT NULL AUTO_INCREMENT,
              nome_cargo VARCHAR(50) UNIQUE NOT NULL ,
              PRIMARY KEY (idt)
        )'''
    cursor.execute(sql_cargo)
    sql_empregado = ''' CREATE TABLE IF NOT EXISTS tb_empregado(
                  idt INT NOT NULL AUTO_INCREMENT,
                  nome_empregado VARCHAR(200) NOT NULL,
                  data_nascimento DATE NULL,
                  genero enum('M', 'F') NOT NULL,
                  cod_cargo int NOT NULL,
                  PRIMARY KEY (idt),
                  FOREIGN KEY(cod_cargo) REFERENCES td_cargo(idt)
            )'''
    cursor.execute(sql_empregado)
def insert_cargo():  #insere um input para adicionar dados na tabela
    var_cargo = input("Digite o nome do cargo:")
    sql = f''' insert into td_cargo   
                (nome_cargo)
                values ('{var_cargo}') '''
    cursor.execute(sql)
    conexao.commit()  #atualiza os registros no banco
def insert_empregado():  #insere um input para adicionar dados na tabela
    var_nome_empregado = input("Digite o nome do empregado:")
    var_data_nascimento = input("Digite a data de nascimento do funcionario:")
    var_genero = input("Digite M para masculino e F para feminino:")
    var_cod_cargo = int(input("Digite o codigo do cargo:"))
    sql = f''' insert into tb_empregado   
                (nome_empregado, data_nascimento, genero, cod_cargo)
                values ('{var_nome_empregado}','{var_data_nascimento}', '{var_genero}',{var_cod_cargo}) '''
    cursor.execute(sql)
    conexao.commit()  #atualiza os registros no banco
def select_all_emp():
    sql = " select * from tb_empregado "
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print("-List of tuplas:")
    print(l_registros)# fetchall pega os resultados e joga numa lista
    for record in l_registros:  # mostra na vertical
        print(record)
    print("-Colunas, notaçao do vetor:")
    for record in l_registros:
        print("-IDT:", record[0])
        print("-Nome empregado:", record[1])
        print("-Data nascimento:", record[2])
        print("-Genero:", record[3])
        print("-Código cargo:", record[4])
if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    insert_cargo()
    insert_empregado()
    select_all_emp()
    close_connection()
