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
from SaCursor import cur as ncur

class BookReg(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BookReg, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.setWindowTitle('Book Inscribtion')
        self.initUI()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
    def initUI(self):
        self.errors=QtGui.QLabel(self)
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


        self.bid_lb=QtGui.QPushButton('Book ID',self)
        self.isbn_lb=QtGui.QPushButton('ISBN',self)
        self.title_lb=QtGui.QPushButton('Title',self)
        self.subject_lb=QtGui.QPushButton('Subject',self)
        self.price_lb=QtGui.QPushButton('Price',self)
        self.pub_date_lb=QtGui.QPushButton('DatePub',self)
        self.pub_date_lb.setFixedSize(75,23)
        self.branch_id_lb=QtGui.QPushButton('Branch ID',self)
        self.publisher_id_lb=QtGui.QPushButton('Publisher ID',self)
        self.num_published_lb=QtGui.QPushButton('NumPub',self)
        self.granter_id_lb=QtGui.QPushButton('Grander ID',self)
        self.granded_date_lb=QtGui.QPushButton('Grant Date',self)
        self.granded_date_lb.setFixedSize(75,23)
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
        self.h12.addWidget(self.errors)
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
    def convertDate(self,date):
        """ converts date to mssql date format """

        first=date.index('/')
        s0=date[:first]
        if len(s0)==1: s0="0"+s0
        tmp=date[first+1:]
        second=tmp.index('/')
        s1=tmp[:second]
        if len(s1)==1: s1="0"+s1
        s2=tmp[second+1:]
        res= s2+"-"+s1+"-"+s0
        return str(res)
    def done(self):
        try:
            comma=','
            BID=str(self.bid_le.text())
            ISBN=str(self.isbn_le.text())
            Title=str(self.title.text())
            Subj=str(self.subject.text())
            PubDate=str(self.convertDate(str(self.pub_date.text())))
            price=str(self.price_le.text())
            branchID=str(self.branch_id_le.text())
            PID=str(self.publisher_id_le.text())
            numP=str(self.num_published.text())
            GID=str(self.granter_id_le.text())
            GDate=str(self.convertDate(str(self.granded_date_le.text())))

            ncur.execute('EXEC BookInsert '+BID+comma+ISBN+comma+Title+comma+Subj+comma+'\''+PubDate+'\''+comma+'\''+price+'\''+comma+branchID+comma+PID+comma+numP+comma+GID+comma+'\''+GDate+'\''+';')
            ncur.commit()
            print 'successfully inserted'
            self.close()
        except:
            self.errors.setText("There are some errors in your inserted fields, fix them and then try again")


class BookBorrow(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BookBorrow, self).__init__(parent)
        self.setWindowTitle("Borrow Book")
        self.cur=cur
        self.type=type
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
    def convertDate(self,date):
        """ converts date to mssql date format """

        first=date.index('/')
        s0=date[:first]
        if len(s0)==1: s0="0"+s0
        tmp=date[first+1:]
        second=tmp.index('/')
        s1=tmp[:second]
        if len(s1)==1: s1="0"+s1
        s2=tmp[second+1:]
        res= s2+"-"+s1+"-"+s0
        return str(res)
    def done(self):

        BID=str(self.bid_le.text())
        MemID=str(self.mem_id_le.text())
        DueD=str(self.convertDate(str(self.due_date_le.text())))

        ncur.execute('EXEC BorrowBook '+BID+','+MemID+',\''+DueD+'\';')
        ncur.commit()
        print 'successful'
        self.close()

class BookRetBorrow(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BookRetBorrow, self).__init__(parent)
        self.setWindowTitle("Return Book")
        self.cur=cur
        self.type=type
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
        self.BBid=str(self.bid_le.text())
        ncur.execute('select Available from book where Bid='+self.BBid)
        flag=ncur.fetchone()[0]
        if flag=='1':
                self.msg_label.setText('The Book is Already Available')
        else:
            ncur.execute('select borrow_mem_id,borrow_due_date from book where Bid='+self.BBid)
            fetch= ncur.fetchall()
            a=fetch[0][0]
            a=str(a)
            print a
            b=fetch[0][1]
            b=str(b)
            print b
            self.mem_id_le.setText(a)
            self.due_date_le.setText(b)
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


    def convertDate(self,date):
        """ converts date to mssql date format """

        first=date.index('/')
        s0=date[:first]
        if len(s0)==1: s0="0"+s0
        tmp=date[first+1:]
        second=tmp.index('/')
        s1=tmp[:second]
        if len(s1)==1: s1="0"+s1
        s2=tmp[second+1:]
        res= s2+"-"+s1+"-"+s0
        return str(res)
    def inscribe(self):
        try:
            RetDate=str(self.convertDate(str(self.retdate_le.text())))
            ncur.execute('EXEC ReturnBook '+self.BBid+',\''+RetDate+'\';')
            ncur.commit()
            print 'successfully returned'
            self.close()
        except:
            self.msg_label.setText('Fatal Error, check Fields')


