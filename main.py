from conexao import criar_conexao, fechar_conexao
 insere_usuario(con, nome, email, senha):
 cursor = con.cursor()
 sql = "INSERT INTO usuario (nome, email, senha) values (%s, %s, %s)"
 valores = (nome, email, senha)
 cursor.execute(sql, valores)
 cursor.close()
    con.commit()

def main():
    con = criar_conexao("127.0.0.1", "root," "", "test")
    
    insere_usuario(con, "teste", "teste@fortlev.com.br", "23abcteste")
def
    
    fechar_conexao(con) 

if __name__== "__main__":
    main() 
	