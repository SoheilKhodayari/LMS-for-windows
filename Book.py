__author__ = 'soheil'
from PyQt4 import QtGui
import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QSplitter, QLabel, QVBoxLayout
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
class BookReg(QWidget):
    def __init__( self, parent=None  ):
        super(BookReg, self).__init__(parent)
        self.initUI()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Done',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.bid_le=QtGui.QLineEdit()
        self.isbn_le=QtGui.QLineEdit()
        self.title=QtGui.QLineEdit()
        self.subject=QtGui.QLineEdit()
        self.price_le=QtGui.QLineEdit()
        self.pub_date=QtGui.QDateEdit()
        self.branch_id_le=QtGui.QLineEdit()
        self.publisher_id_le=QtGui.QLineEdit()
        self.num_published=QtGui.QLineEdit()
        self.granter_id_le=QtGui.QLineEdit()
        self.granded_date_le=QtGui.QDateEdit()
        self.avail_cb = QtGui.QCheckBox('Available', self)

        self.bid_lb=QtGui.QPushButton('Book ID',self)
        self.isbn_lb=QtGui.QPushButton('ISBN',self)
        self.title_lb=QtGui.QPushButton('Title',self)
        self.subject_lb=QtGui.QPushButton('Subject',self)
        self.price_lb=QtGui.QPushButton('Price',self)
        self.pub_date_lb=QtGui.QPushButton('Date Published',self)
        self.branch_id_lb=QtGui.QPushButton('Branch ID',self)
        self.publisher_id_lb=QtGui.QPushButton('Publisher ID',self)
        self.num_published_lb=QtGui.QPushButton('Publishing Number',self)
        self.granter_id_lb=QtGui.QPushButton('Grander ID',self)
        self.granded_date_lb=QtGui.QPushButton('Grant Date',self)
        #self.avail_cb_ = QtGui.QCheckBox('Available', self)



        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.bid_lb)
        self.h1.addWidget(self.bid_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.isbn_lb)
        self.h2.addWidget(self.isbn_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.title_lb)
        self.h3.addWidget(self.title)
        self.h4=QtGui.QHBoxLayout()
        self.h4.addWidget(self.subject_lb)
        self.h4.addWidget(self.subject)
        self.h5=QtGui.QHBoxLayout()
        self.h5.addWidget(self.price_lb)
        self.h5.addWidget(self.price_le)
        self.h6=QtGui.QHBoxLayout()
        self.h6.addWidget(self.pub_date_lb)
        self.h6.addWidget(self.pub_date)
        self.h7=QtGui.QHBoxLayout()
        self.h7.addWidget(self.branch_id_lb)
        self.h7.addWidget(self.branch_id_le)
        self.h8=QtGui.QHBoxLayout()
        self.h8.addWidget(self.publisher_id_lb)
        self.h8.addWidget(self.publisher_id_le)
        self.h9=QtGui.QHBoxLayout()
        self.h9.addWidget(self.num_published_lb)
        self.h9.addWidget(self.num_published)
        self.h10=QtGui.QHBoxLayout()
        self.h10.addWidget(self.granter_id_lb)
        self.h10.addWidget(self.granter_id_le)
        self.h11=QtGui.QHBoxLayout()
        self.h11.addWidget(self.granded_date_lb)
        self.h11.addWidget(self.granded_date_le)
        self.h12=QtGui.QHBoxLayout()
        self.h12.addWidget(self.avail_cb)
        self.h13=QtGui.QHBoxLayout()
        self.h13.addWidget(self.btn_done)


        self.v1=QtGui.QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h7)
        self.v1.addLayout(self.h8)
        self.v1.addLayout(self.h9)
        self.v1.addLayout(self.h10)
        self.v1.addLayout(self.h11)
        self.v1.addLayout(self.h12)
        self.v1.addLayout(self.h13)



        group=QtGui.QGroupBox('Book Registration')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass

class BookBorrow(QWidget):
    def __init__( self, parent=None  ):
        super(BookBorrow, self).__init__(parent)
        self.setWindowTitle("Borrow Book")
        self.initUI()
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Inscribe',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)
        self.bid_le=QtGui.QLineEdit()
        self.mem_id_le=QtGui.QLineEdit()
        self.due_date_le=QtGui.QDateEdit()
        self.bid_lb=QtGui.QPushButton('Book ID',self)
        self.mem_id_lb=QtGui.QPushButton('Member ID',self)
        self.due_date_lb=QtGui.QPushButton('Due Date',self)



        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.bid_lb)
        self.h1.addWidget(self.bid_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.mem_id_lb)
        self.h2.addWidget(self.mem_id_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.due_date_lb)
        self.h3.addWidget(self.due_date_le)
        self.h4=QtGui.QHBoxLayout()
        self.h4.addWidget(self.btn_done)


        self.v1=QtGui.QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h4)


        group=QtGui.QGroupBox('Book Borrow')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass  #set available boolean in database to false

class BookRetBorrow(QWidget):
    def __init__( self, parent=None  ):
        super(BookRetBorrow, self).__init__(parent)
        self.setWindowTitle("Return Book")
        self.initUI()
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Check',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.inscribe_btn=QtGui.QPushButton('Inscribe')
        self.inscribe_btn.resize(self.inscribe_btn.sizeHint())
        self.inscribe_btn.clicked.connect(self.inscribe)

        self.msg_label=QtGui.QLabel(self)
        self.bid_le=QtGui.QLineEdit()
        self.mem_id_le=QtGui.QLineEdit()
        self.mem_id_le.setReadOnly(True)  #load values from db
        self.due_date_le=QtGui.QLineEdit()
        self.due_date_le.setReadOnly(True)
        self.retdate_le=QtGui.QDateEdit()
        self.retdate_lb=QtGui.QPushButton('Return Date')

        self.bid_lb=QtGui.QPushButton('Book ID',self)
        self.mem_id_lb=QtGui.QPushButton('Member ID')
        self.due_date_lb=QtGui.QPushButton('Due Date')



        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.bid_lb)
        self.h1.addWidget(self.bid_le)
        self.h4=QtGui.QHBoxLayout()
        self.h4.addWidget(self.btn_done)
        self.h5=QtGui.QHBoxLayout()
        self.h5.addWidget(self.msg_label)

        self.v1=QtGui.QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h4)
        self.v1.addLayout(self.h5)


        group=QtGui.QGroupBox('Return Book')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass
        #if book is available:
                # set self.msg_label to book is already returned at ret Date
        #else
        self.mem_id_le.setText("member id from Db")
        self.due_date_le.setText("due_date from Db")
        self.h6=QtGui.QHBoxLayout()
        self.h6.addWidget(self.retdate_lb)
        self.h6.addWidget(self.retdate_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.mem_id_lb)
        self.h2.addWidget(self.mem_id_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.due_date_lb)
        self.h3.addWidget(self.due_date_le)
        self.h41=QtGui.QHBoxLayout()
        self.h41.addWidget(self.inscribe_btn)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)
        self.v1.addLayout(self.h6)
        self.v1.addLayout(self.h41)
    def inscribe(self):
        #set returned date
        #also
        #if ret date > due _date set has_penalty to true
        # secretary can cancel the penalty if wants in member cancel penalty panel if a member has penalty
        pass
