__author__ = 'soheil'

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
import sys

class AuthorRegister(QWidget):
    def __init__( self, parent=None  ):
        super(AuthorRegister, self).__init__(parent)
        self.setWindowTitle("Author inscription")
        self.initUI()
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Inscribe',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.author_id_le=QtGui.QLineEdit()
        self.fname_le=QtGui.QLineEdit()
        self.lname_le=QtGui.QLineEdit()
        self.phone_le=QtGui.QLineEdit()
        self.phone_le.setPlaceholderText("Separated By Space")
        self.email_le=QtGui.QLineEdit()
        self.email_le.setPlaceholderText("Separated By Space")
        self.phone_lb=QtGui.QPushButton('Phone',self)
        self.email_lb=QtGui.QPushButton('Email',self)
        self.author_id_lb=QtGui.QPushButton('Author ID',self)
        self.fname_lb=QtGui.QPushButton('First Name',self)
        self.lname_lb=QtGui.QPushButton('Last Name',self)




        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.author_id_lb)
        self.h1.addWidget(self.author_id_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.fname_lb)
        self.h2.addWidget(self.fname_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.lname_lb)
        self.h3.addWidget(self.lname_le)
        self.h5=QtGui.QHBoxLayout()
        self.h5.addWidget(self.phone_lb)
        self.h5.addWidget(self.phone_le)
        self.h6=QtGui.QHBoxLayout()
        self.h6.addWidget(self.email_lb)
        self.h6.addWidget(self.email_le)
        self.h4=QtGui.QHBoxLayout()
        self.h4.addWidget(self.btn_done)


        self.v1=QtGui.QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h4)


        group=QtGui.QGroupBox('Inscription')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass  #set available boolean in database to false

class Compile(QWidget):
    def __init__( self, parent=None  ):
        super(Compile, self).__init__(parent)
        self.setWindowTitle("Compile Book")
        self.initUI()
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Inscribe',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.author_id_le=QtGui.QLineEdit()
        self.bid_le=QtGui.QLineEdit()
        self.author_id_lb=QtGui.QPushButton('Author ID',self)
        self.bid_lb=QtGui.QPushButton('Book ID',self)




        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.author_id_lb)
        self.h1.addWidget(self.author_id_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.bid_lb)
        self.h2.addWidget(self.bid_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.btn_done)
        self.v1=QtGui.QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)

        group=QtGui.QGroupBox('Compile')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass  #set db