# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import sys
import mysql.connector
from mysql.connector import Error

class Ui_Interface(object):      
    
    def __init__(self):
        self.regiao = "%Aveiro%"
        self.regiao1 = None
        database = "BaseGOV"
        tableName = "Contrato"
        self.dbm = DatabaseManager(database, tableName)
    
    def loadData2(self,regiao,adjudicante):
         investimento=dbm.GetInvestimento(regiao,adjudicante)    
         
         self.tabela1.setRowCount(0)
         for row_number, row_data in enumerate(investimento):
            self.tabela1.insertRow(row_number)
            for column_number, investimento in enumerate(row_data):
                self.tabela1.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(investimento)))
    
    def loadData3(self,regiao,adjudicante):
         investimento=dbm.GetInvestimento(regiao,adjudicante)    
         
         self.tabela2.setRowCount(0)
         for row_number, row_data in enumerate(investimento):
            self.tabela2.insertRow(row_number)
            for column_number, investimento in enumerate(row_data):
                self.tabela2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(investimento)))
    
    def loadData4(self,regiao,adjudicante):
         investimento=dbm.GetInvestimento(regiao,adjudicante)    
    
         self.tabela3.setRowCount(0)
         for row_number, row_data in enumerate(investimento):
            self.tabela3.insertRow(row_number)
            for column_number, investimento in enumerate(row_data):
                self.tabela3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(investimento)))
                
    
    def loadData5(self,regiao,adjudicante):
         investimento=dbm.GetInvestimento(regiao,adjudicante)    
        
         self.tabela4.setRowCount(0)
         for row_number, row_data in enumerate(investimento):
            self.tabela4.insertRow(row_number)
            for column_number, investimento in enumerate(row_data):
                self.tabela4.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(investimento)))
                
    
    def loadData6(self,regiao,adjudicante):
         investimento=dbm.GetInvestimento(regiao,adjudicante)    
        
         self.tabela5.setRowCount(0)
         for row_number, row_data in enumerate(investimento):
            self.tabela5.insertRow(row_number)
            for column_number, investimento in enumerate(row_data):
                self.tabela5.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(investimento)))
     
        
    def loadData(self,regiao):
        data = dbm.GetData(regiao)
        
        #print(data)
        self.tabelaLista.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tabelaLista.insertRow(row_number)
            #print(data[0])
            for column_number, data in enumerate(row_data):
               self.tabelaLista.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
        data1 = dbm.GetData(regiao)
        cont = 0
        for cont, row_data1 in enumerate(data1):            
          
            for column_number1, data1 in enumerate(row_data1):
                if (data1 == str(data1)):
                    print(column_number1, data1)
                    if (cont == 0):
                        self.loadData2(regiao,data1)
                        cont +=1
                    if (cont == 1):
                        self.loadData3(regiao,data1)
                        cont +=1
                    if (cont == 2):
                        self.loadData4(regiao,data1)
                        cont +=1
                    if (cont == 3):
                        self.loadData5(regiao,data1)
                        cont +=1
                    if (cont == 4):
                        self.loadData6(regiao,data1)
                        cont +=1
                
               
         
         
    def printButtonPressed(self, nome):
        print(f'printButtonPressed {nome}')
        nome1 =  "%" + nome + "%"
        self.loadData(nome1)
        
    
    def setupUi(self, Interface):
        Interface.setObjectName("Interface")
        Interface.resize(817, 885)
        self.btn_lisboa = QtWidgets.QPushButton(Interface)
        self.btn_lisboa.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.btn_lisboa.setObjectName("btn_lisboa")
        lisboastr = "Lisboa"
        self.btn_lisboa.clicked.connect(lambda: self.printButtonPressed(lisboastr))
        portostr = "Porto"
        self.btn_porto = QtWidgets.QPushButton(Interface)
        self.btn_porto.setGeometry(QtCore.QRect(80, 0, 75, 23))
        self.btn_porto.setObjectName("btn_porto")
        self.btn_porto.clicked.connect(lambda: self.printButtonPressed(portostr))
        bragastr = "Braga"
        self.btn_braga = QtWidgets.QPushButton(Interface)
        self.btn_braga.setGeometry(QtCore.QRect(220, 0, 75, 23))
        self.btn_braga.setObjectName("btn_braga")
        self.btn_braga.clicked.connect(lambda: self.printButtonPressed(bragastr))
        farostr = "Faro"
        self.btn_faro = QtWidgets.QPushButton(Interface)
        self.btn_faro.setGeometry(QtCore.QRect(150, 0, 75, 23))
        self.btn_faro.setObjectName("btn_faro")
        self.btn_faro.clicked.connect(lambda: self.printButtonPressed(farostr))
        aveirostr = "Aveiro"
        self.btn_aveiro = QtWidgets.QPushButton(Interface)
        self.btn_aveiro.setGeometry(QtCore.QRect(290, 0, 75, 23))
        self.btn_aveiro.setObjectName("btn_aveiro")
        self.btn_aveiro.clicked.connect(lambda: self.printButtonPressed(aveirostr))
        self.tabelaLista = QtWidgets.QTableWidget(Interface)
        self.tabelaLista.setGeometry(QtCore.QRect(10, 30, 613, 201))
        self.tabelaLista.setRowCount(5)
        self.tabelaLista.setColumnCount(2)
        self.tabelaLista.setObjectName("tabelaLista")
        col = ["Adjudicante","Investimento"]
        self.tabelaLista.setHorizontalHeaderLabels(col)
        hh = self.tabelaLista.horizontalHeader()
        hh.setDefaultSectionSize(298)

        self.retranslateUi(Interface)
        QtCore.QMetaObject.connectSlotsByName(Interface)

        
        #Tabelas novas em baixo
        self.tabela1 = QtWidgets.QTableWidget(Interface)
        self.tabela1.setGeometry(QtCore.QRect(10, 240, 1200, 121))
        self.tabela1.setRowCount(3)
        self.tabela1.setColumnCount(3)
        self.tabela1.setObjectName("tabela1")
        col = ["Adjudicante","Investimento", "Contrato"]
        self.tabela1.setHorizontalHeaderLabels(col)
        hh = self.tabela1.horizontalHeader()
        hh.setDefaultSectionSize(298)
        header = self.tabela1.horizontalHeader()
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.tabela2 = QtWidgets.QTableWidget(Interface)
        self.tabela2.setGeometry(QtCore.QRect(10, 370, 1200, 121))
        self.tabela2.setRowCount(3)
        self.tabela2.setColumnCount(3)
        self.tabela2.setObjectName("tabela2")
        col = ["Adjudicante","Investimento", "Contrato"]
        self.tabela2.setHorizontalHeaderLabels(col)
        hh = self.tabela2.horizontalHeader()
        hh.setDefaultSectionSize(298)
        header = self.tabela2.horizontalHeader()
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.tabela3 = QtWidgets.QTableWidget(Interface)
        self.tabela3.setGeometry(QtCore.QRect(10, 500, 1200, 121))
        self.tabela3.setRowCount(3)
        self.tabela3.setColumnCount(3)
        self.tabela3.setObjectName("tabela3")
        col = ["Adjudicante","Investimento", "Contrato"]
        self.tabela3.setHorizontalHeaderLabels(col)
        hh = self.tabela3.horizontalHeader()
        hh.setDefaultSectionSize(298)
        header = self.tabela3.horizontalHeader()
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.tabela4 = QtWidgets.QTableWidget(Interface)
        self.tabela4.setGeometry(QtCore.QRect(10, 630, 1200, 121))
        self.tabela4.setRowCount(3)
        self.tabela4.setColumnCount(3)
        self.tabela4.setObjectName("tabela4")
        col = ["Adjudicante","Investimento", "Contrato"]
        self.tabela4.setHorizontalHeaderLabels(col)
        hh = self.tabela4.horizontalHeader()
        hh.setDefaultSectionSize(298)
        header = self.tabela4.horizontalHeader()
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.tabela5 = QtWidgets.QTableWidget(Interface)
        self.tabela5.setGeometry(QtCore.QRect(10, 760, 1200, 121))
        self.tabela5.setRowCount(3)
        self.tabela5.setColumnCount(3)
        self.tabela5.setObjectName("tabela5")
        col = ["Adjudicante","Investimento", "Contrato"]
        self.tabela5.setHorizontalHeaderLabels(col)
        hh = self.tabela5.horizontalHeader()
        hh.setDefaultSectionSize(298)
        header = self.tabela5.horizontalHeader()
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        
    def retranslateUi(self, Interface):
        _translate = QtCore.QCoreApplication.translate
        Interface.setWindowTitle(_translate("Interface", "Segundo Momento PI"))
        self.btn_lisboa.setText(_translate("Interface", "Lisboa"))
        self.btn_porto.setText(_translate("Interface", "Porto"))
        self.btn_braga.setText(_translate("Interface", "Braga"))
        self.btn_faro.setText(_translate("Interface", "Faro"))
        self.btn_aveiro.setText(_translate("Interface", "Aveiro"))
        
                
        

class DatabaseManager: 
    def __init__(self, database, tableName):
        self.db = database
        self.tableName = tableName

        
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "BaseGOV",
        passwd = "123456")
        
        self.cursor = self.conn.cursor()
        self.ConnectToDatabase()
        
    def ConnectToDatabase(self):
        try:
            self.conn.database = self.db
            print(f"Connected to database {self.db}")
        except mysql.connector.Error as err:
            print(err.msg)


    def GetData(self, regiao):
        #print(regiao)
        return self.RunCommand("select * from(select adjudicante, sum(valorContratual) as ti from Contrato where regiao like '%s' group by adjudicante) as Ordenação order by ti desc limit 5;" % regiao)

    def GetInvestimento(self, regiao,adjudicante):
        #print(regiao,adjudicante)
        manutenção = "Manutenção"
        ornecimento = "ornecimento"
        return self.RunCommand("select * from(select adjudicante, valorContratual, objetoContratual, regiao from Contrato where objetoContratual not like '%s' and objetoContratual not like '%s') as Investimentos where adjudicante = '%s' and regiao like '%s' order by valorContratual desc limit 3;" %(manutenção,ornecimento,adjudicante,regiao))
         
    
    def RunCommand(self, cmd):
        #print ("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print ('ERROR MESSAGE: ' + str(err.msg))
            print ('WITH ' + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg

if __name__ == "__main__":
    print(sys.executable)
    db = 'BaseGOV'
    tableName = 'Contrato'
    
    dbm = DatabaseManager(db, tableName)
    print(dbm.conn.get_server_info())
    #clm = GetColumns()
    
    app = QtWidgets.QApplication(sys.argv)
    Interface = QtWidgets.QWizardPage()
    ui = Ui_Interface()
    ui.setupUi(Interface)
    Interface.show()
    sys.exit(app.exec_())