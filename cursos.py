import pymysql
import os

class App:

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='test'
        )
        self.cursos = self.conn.cursor()


        def inserir(self):
            name = input("inserir um nome: \n")
            sql = "insert into code(DEVOPS) values('{}')".format(name)
            print(sql)
            self.cursor.execute(sql)
            print("conexão sucedida \n")
            self.conn.commit()
            os.system('pause')


            
            aplication = App()
            aplication.insertar()
        