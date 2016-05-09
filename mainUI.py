from SaCursor import cur as ncur
from PyQt4 import QtGui
import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QSplitter, QLabel, QVBoxLayout
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from SaCursor import cur as ncur
from table import *
import os


class MyTable(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(MyTable, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
        self.executeAction()
    def initUI(self):
        self.Btb=None
        self.Mtb=None
        self.data=None
        self.searchType_le=QtGui.QLineEdit()
        self.searchType_le.setReadOnly(True)
        self.searchField_le=QtGui.QLineEdit()
        self.searchField_le.setPlaceholderText('')
        self.searchField_lb=QtGui.QPushButton('SearchField',self)
        self.searchType = QtGui.QComboBox(self)
        self.searchType.setFixedSize(78,23)
        self.searchType.addItem("All Books")
        self.searchType.addItem("ByID")
        self.searchType.addItem("ByTitle")
        self.searchType.addItem("ByAuthor")
        self.searchType.activated[str].connect(self.onActivated)

        self.execute=QtGui.QPushButton('execute',self)
        # self.timer = QtCore.QTimer(self)
        # self.timer.start(10)
        # self.timer.timeout.connect(self.Hover)

        self.execute.clicked.connect(self.executeAction)

        hds=QtGui.QHBoxLayout()
        self.lbl1=QtGui.QLabel()
        hds.addWidget(self.lbl1)
        hq=QtGui.QHBoxLayout()
        self.lbl=QtGui.QLabel()
        hq.addWidget(self.lbl)
        h1=QtGui.QHBoxLayout()
        h1.addWidget(self.searchType)
        h1.addWidget(self.searchType_le)
        h2=QtGui.QHBoxLayout()
        h2.addWidget(self.searchField_lb)
        h2.addWidget(self.searchField_le)
        h3=QtGui.QHBoxLayout()
        h3.addWidget(self.execute)
        self.v=QtGui.QVBoxLayout()
        self.v.addLayout(h1)
        self.v.addLayout(h2)
        self.v.addLayout(hq)
        self.v.addLayout(h3)

        self.group=QtGui.QGroupBox('Book Search')
        self.group.setLayout(self.v)
        self.Vbox=QtGui.QVBoxLayout()
        self.Vbox.addLayout(hds)
        self.Vbox.addWidget(self.group)

        self.setLayout(self.Vbox)
    # def Hover(self):
    #     self.timer.start(10)
    #     if self.execute.underMouse() == True:
    #         self.execute.setStyleSheet("font-size:40px;background-color:#444444;\
    #         border: 2px solid #333333")
    #     else:
    #         self.execute.setStyleSheet("font-size:40px;background-color:#333333;\
    #         border: 2px solid #222222")



    def executeAction(self):
        self.lbl.setText("")
        self.opcode=None
        t=str(self.searchType_le.text())
        if t=="All Books": self.opcode=0
        elif t=="ByID": self.opcode=1
        elif t=="ByTitle": self.opcode=2
        elif t=="ByAuthor": self.opcode=3
        else: self.opcode=0

        field=str(self.searchField_le.text())

        if self.opcode==0:
            try:
                ncur.execute("select * from getBookList()")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        elif self.opcode==1:
            try:
                ncur.execute("select * from getBookListById("+field+")")
                self.data=ncur.fetchall()
            except:
                print "               No results were found, Please Search a More Precise Value."
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==2:
            try:
                ncur.execute("select * from getBookListByTitle("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==3:
            try:
                ncur.execute("select * from getBookListByAuthor("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        if len(self.data)!=0:
            if self.Btb is None:
                self.lbl.setText("")
                if self.opcode!=3:
                    self.Btb=sTable(self.data)
                else:
                    self.Btb=AuthTable(self.data)
            else:
                self.lbl.setText("")
                self.Btb.setParent(None)
                if self.opcode!=3:
                    self.Btb=sTable(self.data)
                else:
                    self.Btb=AuthTable(self.data)

            self.Vbox.addWidget(self.Btb)
        else:
            self.lbl.setText("               No results were found, Please Search a More Precise Value.")
            print 'no results were found'


    def onActivated(self,text):   #self.combo3.currenttext() also catches its selection
        self.searchType_le.setText(text)


