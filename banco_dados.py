import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root', password='', host='127.0.0.1')
    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE if not exists db_concessionaria"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')
def create_connection():
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='db_concessionaria')
    print('Conexão:', con)
    return con
def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')
def create_table():
    sql = """ CREATE TABLE if not exists tb_carros(
    idt INT NOT NULL AUTO_INCREMENT UNIQUE,    
    carro VARCHAR(45) NOT NULL UNIQUE,  
    preco DECIMAL(9,2) NOT NULL,       
    dta_fabricacao DATE NULL,  
    cor_carro VARCHAR(30) NULL
    PRIMARY KEY (idt)                  
    )   """
    cursor.execute(sql)
def insert_database():
    carro = input('Insert - Nome: ')
    preco = float(input('Preço: '))
    data_fabricacao = input('Data: aaaa-mm-dd: ')
    cor = input('Cor do carro:')
    sql = f""" insert into tb_produto (nome, preco, dta_validade) 
                      values ('{carro}', {preco}, '{data_fabricacao}, {cor}')  """
    cursor.execute(sql)
    conexao.commit()
def select_database():
    print('- Consulta:')
    sql = ' select * from tb_produto '
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print('- List of tuplas:')
    print(l_registros)
    print(' - Tuplas:')
    for record in l_registros:
        print(record)
    print("- Colunas, notação de vetor:")
    for record in l_registros:
        print("- Idt:", record[0])
        print("Nome:", record[1])
        print("Preço:", record[2])
        print('Data de frabricação:', record[3])
        print('Cor do carro:', record[4])
def delete_database():
    nome_carro = input('Digite o carro que deseja deletar:')
    sql = f"DELETE FROM tb_carros WHERE carro = {nome_carro}"
    cursor.execute(sql)
    conexao.commit()
    print('Carro deletado com sucesso')
def main():
    create_database
    conexao = create_connection()
    global cursor
    cursor = conexao.cursor()
    create_table()
    while True:
        print("\nMenu:")
        print("1.Inserir produto:")
        print("2.listar produtos:")
        print("3.deletar produto:")
        print("sair.")

        opcao = int(input("\nDigite a opção desejada"))
        if opcao == 1:
            insert_database()
        elif opcao == 2:
            select_database()
        elif opcao == 3:
            delete_database()
        elif opcao == 4:
            close_connection()
        else:
            print("Opção inválida. Por favor digite uma opção válida")
if __name__ == '__main__':
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    insert_database()
    select_database()
    close_connection()
