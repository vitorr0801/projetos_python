import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1')
    print('Conexão:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE if not exists db_cadastro"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')
def create_connection():
    con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'db_cadastro')
    print('Conexão:', con)
    return con
def create_tables():
    sql_cargo = """CREATE TABLE IF NOT EXISTS td_cargo(idt int NOT NULL AUTO_INCREMENT,
                                            nome varchar(45) UNIQUE NOT NULL,
                                            PRIMARY KEY (idt))"""
    sql_empregado = """ CREATE TABLE IF NOT EXISTS tb_empregado(idt int NOT NULL AUTO_INCREMENT,
                                                                nome varchar(45) NOT NULL,
                                                                dta_nascimento date NULL,
                                                                genero enum('M', 'F') NOT NULL,
                                                                cod_cargo int NOT NULL,
                                                                PRIMARY KEY (idt),
                                                                FOREIGN KEY(cod_cargo) REFERENCES td_cargo(idt))"""
    cursor.execute(sql_cargo)
    cursor.execute(sql_empregado)
def insert_cargo():
    nome_cargo = input("Informe o cargo do empregado:")
    sql = f"""  insert into td_cargo (nome)
                values('{nome_cargo}')"""
    cursor.execute(sql)
    conexao.commit()
def insert_empregado():
    nome_empregado = input("Digite o nome do funcionário:")
    dta_nascimento = input("Digite a data de nascimento do empregado:")
    genero = input("Digite M para masculino, F para feminino:")
    cod_cargo = int(input("Digite o código do cargo do empregado:"))
    sql = f"""  insert into tb_empregado (nome, dta_nascimento, genero, cod_cargo)
                values('{nome_empregado}', '{dta_nascimento}', '{genero}', {cod_cargo})"""
    cursor.execute(sql)
    conexao.commit()
def select_all_empregados():
    sql = ''' select * from tb_empregado '''
    cursor.execute(sql)
    registros = cursor.fetchall()
    print(registros)
    print("- Lista de empregados:")
    for record in registros:
        print(record)
    for record in registros:
        print("Idt:", record[0])
        print("Nome:", record[1])
        print("Data nascimento:", record[2])
        print("Gênero:", record[3])
        print("Código do cargo:", record[4])
        print("------------------------------")

def select_all_join():
   sql = """SELECT t1.nome, t2.nome, t2.dta_nascimento, t2.genero, t2.cod_cargo
          from td_cargo as t1 join tb_empregado as t2
          where t1.nome = t2.cod_cargo"""
   cursor.execute(sql)
   registros = cursor.fetchall()
   print(registros)
   for record in registros:
       print("Nome:", record[0])
       print("Data nascimento:", record[1])
       print("Gênero:", record[2])
       print("Código do cargo:", record[3])
def delete_emp():
    nome_empregado = input("Digite o nome do empregado que deseja deletar:")
    sql = f"""DELETE FROM tb_empregado WHERE nome = '{nome_empregado}'"""
    cursor.execute(sql)
    conexao.commit()
    print("Empregado excluído com sucesso.")

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')
if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_tables()
    insert_cargo()
    insert_empregado()
    select_all_empregados()
    select_all_join()
    delete_emp()
    close_connection()