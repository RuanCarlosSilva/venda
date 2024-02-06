from PySide6.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem,QApplication
from ui_main import Ui_MainWindow
from database import Data_base

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cliente")

        #Botões
        self.btn_cadastrar.clicked.connect(self.cadastro_cliente)
        self.btn_pesquisar.clicked.connect(self.pesquisar_cliente)
        self.btn_excluir.clicked.connect(self.excluir_cliente)
        self.btn_editar.clicked.connect(self.alterar_cliente)
        self.tableWidget.cellClicked.connect(self.selecionar_cliente) #busca os valores do banco clicando duas vezes na tabela

#conectar ao banco de dados e criar a tabela de cliente
        self.db = Data_base()
        self.db.connect()
        self.db.criate_table_cliente()

    def closeEvent(self, event):
        self.db.close_connection()
    #fechar a conexão com o banco após fechar a aplicação
    
    def show_message(self,title,message,icon=QMessageBox.information):
        msg = QMessageBox()
        # msg.setIcon(icon) #não está sendo utilizado, porque não há icones nos botões
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()
    
    def cadastro_cliente(self):
        #obter dados dos campos de entrada do forms
        nome = self.nome_txt.text()
        cpf = self.cpf_txt.text()

        #verificação de compos vazios
        if nome.strip()=="" or cpf.strip()=="":
            self.show_message("Atenção","Preencha todos os campos.")
            return
        
        #realizar o cadastro do cliente
        resp =self.db.cadastro_cliente((nome,cpf))

        #recebimento da resposta do banco de dados
        if resp == "ok":
            self.show_message("Cadastro realizado","Cadastro Finalizado!")
        else:
            self.show_message("Erro","Erro ao cadastrar cliente! Verefique as informações.")
    
    def pesquisar_cliente(self):
       
        cpf = self.cpf_txt.text()
 
        # Realizar a pesquisa do cliente
        if not cpf.strip():  # Verifica se o CPF está vazio
            resultados = self.db.pesquisa_cliente()  # Pesquisa todos os clientes caso esteja vazio
        else:
            resultados = self.db.pesquisa_cliente(cpf) # faz a pesquisa espefífica
 
        if resultados:
            self.exibir_resultados(resultados)
        else:
            self.show_message("Atenção", "Clientes não encontrados")
 
    def exibir_resultados(self, resultados):
        # Limpar a tabela antes de exibir novos resultados
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
 
        # Preencher a tabela com os resultados que vierem do banco de dados
        for row, data in enumerate(resultados):
            self.tableWidget.insertRow(row)
            for col, value in enumerate(data):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

    def excluir_cliente(self):
        cpf = self.cpf_txt.text()
 
        if not cpf.strip():  # Verificar se o CPF está vazio
            self.show_message("Atenção", "Por favor, insira o CPF do cliente a ser excluído.")
            return
 
        excluir_msg = QMessageBox.question(self, 'Excluir Cliente',
            f'Tem certeza que deseja excluir o cliente com o CPF {cpf}?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
        if excluir_msg == QMessageBox.Yes:  # Se a resposta for sim , Excluir o cliente
            if self.db.excluir_cliente(cpf):
                self.show_message("Exclusão realizada", "Cliente excluído com sucesso.")
                self.limpar_campos()
                self.tableWidget.clearContents() #Limpa a tabela após a exclusão de dados
                self.tableWidget.setRowCount(0)
               
            else:
                self.show_message("Erro", "Erro ao excluir o cliente.")

    def alterar_cliente(self):
        cpf = self.cpf_txt.text()
 
        if not cpf.strip():          #Verifica se o campo vazio
            self.show_message("Atenção", "Insira um cpf para ser alterado")
            return
        #Obter dados do cliente no campo de entrada
        nome_cli = self.nome_txt.text()
        cpf_cli = self.cpf_txt.text()
 
        #Verificar se os campos estão vazios
        if not nome_cli.strip() or not cpf_cli.strip():
            self.show_message("Atenção", "Preencha os campos par alterar")
            return
 
        if self.db.alterar_cliente(cpf, nome_cli, cpf_cli):
            self.show_message("Alteração", "Alterado com sucesso")
            self.pesquisar_cliente()
        else:
            self.show_message("Erro ao alterar", "Não é possível alterar cliente")
 
    def limpar_campo(self):
        self.nome_txt.clear()
        self.cpf_txt.clear()
 
   
    def selecionar_cliente(self, row, col):
        #Obter dados da linha clicada
        nome_Cliente = self.tableWidget.item(row, 0).text()
        cpf_Cliente = self.tableWidget.item(row, 1).text()
        #Preencher campos de texto com dados obtidos
        self.nome_txt.setText(nome_Cliente)
        self.cpf_txt.setText(cpf_Cliente)

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)

    #criar e exibir a janela principal
    window =MainWindow()
    window.show()

    #executa os eventos dos aplicativos
    sys.exit(app.exec())