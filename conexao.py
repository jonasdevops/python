import mysql.connector

def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=test)


def fechar_conexao(con):
    return con.close()