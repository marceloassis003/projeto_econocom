from PyQt5 import uic,QtWidgets 
import mysql.connector


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="projeto_econocom"
) 
def segunda_tela():
    tela_clientes.show()

def terceira_tela():
    tela_produtos.show()

def quarta_tela():
    tela_pedidos.show()


# cliente
def cadastro_clientes():
    linha1 = tela_clientes.lineEdit.text()
    linha2 = tela_clientes.lineEdit_2.text()
    linha3 = tela_clientes.lineEdit_3.text()

    print("Id_cliente:", linha1)
    print("Nome:", linha2)
    print("Telefone:", linha3)


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO clientes (id_cliente, nome, telefone) values (%s, %s, %s)"
    dados = (str(linha1), str(linha2) , str(linha3))
    cursor.execute(comando_SQL, dados)
    cursor.close()
    banco.commit() 
    tela_clientes.lineEdit.setText("")
    tela_clientes.lineEdit_2.setText("")
    tela_clientes.lineEdit_3.setText("") 

def deletar_clientes():
    linha = tela_lista_clientes.tableWidget.currentRow()
    tela_lista_clientes.tableWidget.removeRow(linha)


    cursor = banco.cursor()
    cursor.execute("SELECT id_cliente FROM clientes")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM clientes WHERE id_cliente="+ str(valor_id))
    banco.commit() 

         
def exibir_clientes(): # dentro da tela clientes exibi uma lista pode chamar de TELA LISTA CLIENTES
    tela_lista_clientes.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM clientes"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    

    tela_lista_clientes.tableWidget.setRowCount(len(dados_lidos))
    tela_lista_clientes.tableWidget.setColumnCount(3)


    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_lista_clientes.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

######################################################################################################

# produtos 
def cadastro_produtos():
    linha1 = tela_produtos.lineEdit.text()
    linha2 = tela_produtos.lineEdit_2.text()
    linha3 = tela_produtos.lineEdit_3.text()

    print("ID_PRODUTO:", linha1)
    print("NOME:", linha2)
    print("PRECO_UNIT:", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (id_produto, nome, preco_unit) values (%s, %s, %s)"
    dados = (str(linha1), str(linha2) , str(linha3))
    cursor.execute(comando_SQL, dados)
    cursor.close()
    banco.commit() 
    tela_produtos.lineEdit.setText("")
    tela_produtos.lineEdit_2.setText("")
    tela_produtos.lineEdit_3.setText("")

def deletar_produto():
    linha = tela_lista_produtos.tableWidget.currentRow()
    tela_lista_produtos.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id_produto FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id_produto="+ str(valor_id))
    banco.commit() 


def exibir_produtos():
    tela_lista_produtos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    tela_lista_produtos.tableWidget.setRowCount(len(dados_lidos))
    tela_lista_produtos.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_lista_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# pedidos

def cadastro_pedidos():
    linha1 = tela_pedidos.lineEdit.text()
    linha2 = tela_pedidos.lineEdit_2.text()
    linha3 = tela_pedidos.lineEdit_3.text()

    print("ID_PEDIDO:", linha1)
    print("ID_CLIENTE:", linha2)
    print("VALOR:", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pedidos (id_pedido, id_cliente, valor) values (%s, %s, %s)"
    dados = (str(linha1), str(linha2) , str(linha3))
    cursor.execute(comando_SQL, dados)
    cursor.close()
    banco.commit() 
    tela_pedidos.lineEdit.setText("")
    tela_pedidos.lineEdit_2.setText("")
    tela_pedidos.lineEdit_3.setText("")

def exibir_pedidos():
    tela_resumo_pedido.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pedidos, clientes WHERE pedidos.id_cliente = clientes.id_cliente "
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    tela_resumo_pedido.tableWidget.setRowCount(len(dados_lidos))
    tela_resumo_pedido.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_resumo_pedido.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))








#CARREGANDO AS TELAS
app=QtWidgets.QApplication([])
tela_home=uic.loadUi("tela_home.ui")
tela_clientes=uic.loadUi("tela_clientes.ui")
tela_lista_clientes=uic.loadUi("tela_lista_clientes.ui")
tela_produtos=uic.loadUi("tela_produtos.ui")
tela_lista_produtos=uic.loadUi("tela_lista_produtos.ui")
tela_pedidos=uic.loadUi("tela_pedidos.ui")
tela_resumo_pedido=uic.loadUi("tela_resumo_pedido.ui")
# carregando as telas atraves do home
tela_home.BtClientes.clicked.connect(segunda_tela)
tela_home.BtProdutos.clicked.connect(terceira_tela)
tela_home.BtPedidos.clicked.connect(quarta_tela)


#botoes tela cliente
tela_clientes.BtInsert.clicked.connect(cadastro_clientes)
tela_clientes.BtListar.clicked.connect(exibir_clientes) #dentro da tela clientes
tela_lista_clientes.BtDelete.clicked.connect(deletar_clientes)

#botoes tela produtos
tela_produtos.BtInsert.clicked.connect(cadastro_produtos)
tela_produtos.BtListar.clicked.connect(exibir_produtos) #dentro da tela de produtos
tela_lista_produtos.BtDelete.clicked.connect(deletar_produto)

#botoes tela pedidos
tela_pedidos.BtInsert.clicked.connect(cadastro_pedidos)
tela_pedidos.BtListar.clicked.connect(exibir_pedidos)



tela_home.show()
app.exec()




















""" 
banco de dados

database projeto_econocom


CREATE TABLE CLIENTES (
ID_CLIENTE INTEGER,
NOME VARCHAR(50) NOT NULL, 
TELEFONE CHAR(50),
PRIMARY KEY(ID_CLIENTE)
);


CREATE TABLE PRODUTOS (
ID_PRODUTO INTEGER, 
NOME VARCHAR(50) NOT NULL, 
PRECO_UNIT FLOAT CHECK(PRECO_UNIT>0), 
PRIMARY KEY(ID_PRODUTO)
);


CREATE TABLE PEDIDOS (
ID_PEDIDO INTEGER, 
ID_CLIENTE INTEGER,
VALOR FLOAT CHECK(VALOR>0), 
PRIMARY KEY(ID_PEDIDO), 
FOREIGN KEY(ID_CLIENTE)
REFERENCES CLIENTES(ID_CLIENTE)
);

CREATE TABLE PEDIDOS_PRODUTOS (
ID_PEDIDO INTEGER NOT NULL, 
ID_PRODUTO INTEGER NOT NULL, 
QTDE INTEGER CHECK(QTDE>0),
PRIMARY KEY (ID_PEDIDO, ID_PRODUTO),
FOREIGN KEY(ID_PEDIDO)
REFERENCES PEDIDOS(ID_PEDIDO),
FOREIGN KEY(ID_PRODUTO) 
REFERENCES PRODUTOS(ID_PRODUTO)
);
 """




















