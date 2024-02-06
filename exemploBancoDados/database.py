import sqlite3

class Data_base:
    def __init__(self,name="empresa.db") -> None:
        self.name=name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(f"Erro ao fechar conexão:{e}")
    
    def criate_table_cliente(self):
        cursor=self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes(
                       id integer primary key autoincrement, 
                       nome_cli text,
                       cpf_cli text);""")
        
    def cadastro_cliente(self,fullDataSet):
        campo_tabela = ('nome_cli','cpf_cli')
        placeholders = ",".join(["?"]*len(campo_tabela))
        sql = f"insert into Clientes({','.join(campo_tabela)}) \
        values ({placeholders})"

        cursor = self.connection.cursor()
        try:
            cursor.execute(sql,fullDataSet)
            self.connection.commit()
            return "ok"
        except Exception as e:
            print(f"Erro ao cadastrar o cliente: {e}")
            return "Erro"
    
    def pesquisa_cliente(self, cpf = None):
        cursor = self.connection.cursor()

        if cpf is None:
            cursor.execute("SELECT nome_cli,cpf_cli from Clientes")
        else: 
            cursor.execute("SELECT nome_cli,cpf_cli from Clientes where cpf_cli =?",(cpf,)) 
            
        result = cursor.fetchall() #retorna todos os resultados encontrados
        return result
    
    def excluir_cliente(self, cpf):
        cursor = self.connection.cursor()
 
        try:
            cursor.execute("DELETE FROM Clientes WHERE cpf_cli = ?", (cpf,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            return False
        
    def alterar_cliente(self, cpf, nome_cli, cpf_cli):
        cursor = self.connection.cursor()
        try:
            cursor.execute("update Clientes set nome_cli = ?, cpf_cli = ? where cpf_cli = ?", (nome_cli, cpf_cli, cpf))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir cliente:{e}")
            return False