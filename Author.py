__author__ = 'soheil'

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
import sys
from table import AuthorTable
from SaCursor import cur as ncur
class AuthorRegister(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(AuthorRegister, self).__init__(parent)
        self.setWindowTitle("Author inscription")
        self.initUI()
        self.cur=cur
        self.type=type
    def initUI(self):
        self.errors=QtGui.QLabel(self)
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
        self.v1.addWidget(self.errors)


        group=QtGui.QGroupBox('Inscription')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        Comma=','


        try:
            authID=str(self.author_id_le.text())
            fname=str(self.fname_le.text())
            lname=str(self.lname_le.text())
            phones=str(self.phone_le.text()).split()
            emails=str(self.email_le.text()).split()
            ncur.execute('EXEC AuhtorInsert '+authID+Comma+fname+Comma+lname+';Commit;')
            for phone in phones:
                 ncur.execute('EXEC AuthorPhoneInsert '+authID+Comma+'\"' +phone +'\"' +';Commit;')
            for email in emails:
                 ncur.execute('EXEC AuthorEmailInsert '+authID+Comma+'\"'+email+'\"'+';Commit;')
            print 'Author inserted Successfully'
            self.close()

        except:
             self.errors.setText("There are some errors in your inserted fields, fix them and then try again")


class Compile(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(Compile, self).__init__(parent)
        self.setWindowTitle("Compile Book")

        self.initUI()
    def initUI(self):
        self.errors=QtGui.QLabel(self)
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
        self.v1.addWidget(self.errors)

        group=QtGui.QGroupBox('Compile')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        try:
            AID=str(self.author_id_le.text())
            ncur.execute('select author_id from Author where author_id='+AID)
            AID_Exists=ncur.fetchone()
            BID=str(self.bid_le.text())
            ncur.execute('select Bid from Book where Bid='+BID)
            BID_Exists=ncur.fetchone()

            if (BID_Exists is not None) and (AID_Exists is not None):
                 ncur.execute('Insert into Compile values('+BID+','+AID+');')
                 ncur.commit()
                 print 'executed successfully'
                 self.close()
            else:
                self.errors.setText("There's Either No Book or Author, Create One and Try Again")

        except:
            self.errors.setText('Wrong Givens, try Again')


class AuthorSearch(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(AuthorSearch, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.setWindowTitle('Author Search')
        self.initUI()
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
        self.searchType.setFixedSize(75,23)
        self.searchType.addItem("AuthorList")
        self.searchType.addItem("ByID")
        self.searchType.addItem("ByFname")
        self.searchType.addItem("ByLname")
        self.searchType.activated[str].connect(self.onActivated)

        self.execute=QtGui.QPushButton('execute',self)
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

        self.group=QtGui.QGroupBox('Author Search')
        self.group.setLayout(self.v)
        self.Vbox=QtGui.QVBoxLayout()
        self.Vbox.addLayout(hds)
        self.Vbox.addWidget(self.group)

        self.setLayout(self.Vbox)




    def executeAction(self):
        self.lbl.setText("")
        self.opcode=None
        t=str(self.searchType_le.text())
        if t=="AuthorList": self.opcode=0
        elif t=="ByID": self.opcode=1
        elif t=="ByFname": self.opcode=2
        elif t=="ByLname": self.opcode=3
        else: self.opcode=0

        field=str(self.searchField_le.text())

        if self.opcode==0:
            try:
                ncur.execute("select * from getAuthorList()")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        elif self.opcode==1:
            try:
                ncur.execute("select * from getAuthorById("+field+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==2:
            try:
                ncur.execute("select * from getAuthorListByFName("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==3:
            try:
                ncur.execute("select * from getAuthorListBylName("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        if len(self.data)!=0:
            if self.Btb is None:
                self.lbl.setText("")
                if self.opcode!=3:
                    self.Btb=AuthorTable(self.data)
                else:
                    self.Btb=AuthorTable(self.data)
            else:
                self.lbl.setText("")
                self.Btb.setParent(None)
                if self.opcode!=3:
                    self.Btb=AuthorTable(self.data)
                else:
                    self.Btb=AuthorTable(self.data)

            self.Vbox.addWidget(self.Btb)
        else:
            self.lbl.setText("               No results were found, Please Search a More Precise Value.")
            print 'no results were found'


    def onActivated(self,text):
        self.searchType_le.setText(text)



class AuthContact(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(AuthContact, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Author Contact')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Author ID:')
        self.id_le=QtGui.QLineEdit()
        self.contact_le=QtGui.QTextEdit()
        self.contact_le.setReadOnly(True)
        self.execbtn=QtGui.QPushButton('execute')
        self.execbtn.clicked.connect(self.done)

        h1=QtGui.QHBoxLayout()
        h1.addWidget(self.id_lb)
        h1.addWidget(self.id_le)
        h2=QtGui.QHBoxLayout()
        h2.addWidget(self.execbtn)
        h3=QtGui.QHBoxLayout()
        h3.addWidget(self.error_lb)
        h4=QtGui.QHBoxLayout()
        h4.addWidget(self.contact_le)

        vb=QtGui.QVBoxLayout()
        vb.addLayout(h1)
        vb.addLayout(h2)
        vb.addLayout(h3)
        vb.addLayout(h4)
        group=QtGui.QGroupBox('Contact')
        group.setLayout(vb)

        hbox=QtGui.QHBoxLayout()
        hbox.addWidget(group)
        self.setLayout(hbox)


    def done(self):
        flag=True
        cont_dict=dict()
        cont_dict['mailList']=''
        cont_dict['phoneList']=''

        bid=str(self.id_le.text())


        if bid=='':
            bid=None
            self.error_lb.setText('Please enter the Author ID Properly')
            self.contact_le.setText('')
        if bid is not None:
                try:
                    ncur.execute('select author_id from author where author_id='+bid)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Author ID')
                    self.contact_le.setText('')
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Author ID')
                    self.contact_le.setText('')



        if bid is not None and flag:
                self.error_lb.setText('')

                ncur.execute('select email_address from author_email where author_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['mailList']+='    '+str(elm[0])+'\n'


                ncur.execute('select * from author_phone where author_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['phoneList']+='    '+str(elm[1])+'\n'



                text='Phones: \n' + cont_dict['phoneList'] + '\n' \
                     'Mails: \n' + cont_dict['mailList']



                self.contact_le.setText(text)


class AuthDelete(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(AuthDelete, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Author Deletion')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Author ID:')
        self.id_le=QtGui.QLineEdit()
        self.res_le=QtGui.QTextEdit()
        self.res_le.setText('Result:'+'\n')
        self.res_le.setReadOnly(True)
        self.execbtn=QtGui.QPushButton('execute')
        self.execbtn.clicked.connect(self.done)

        h1=QtGui.QHBoxLayout()
        h1.addWidget(self.id_lb)
        h1.addWidget(self.id_le)
        h2=QtGui.QHBoxLayout()
        h2.addWidget(self.execbtn)
        h3=QtGui.QHBoxLayout()
        h3.addWidget(self.error_lb)
        h4=QtGui.QHBoxLayout()
        h4.addWidget(self.res_le)

        vb=QtGui.QVBoxLayout()
        vb.addLayout(h1)
        vb.addLayout(h2)
        vb.addLayout(h3)
        vb.addLayout(h4)
        group=QtGui.QGroupBox('Removal')
        group.setLayout(vb)

        hbox=QtGui.QHBoxLayout()
        hbox.addWidget(group)
        self.setLayout(hbox)


    def done(self):
        flag=True
        insID=str(self.id_le.text())

        if insID=='':
            insID=None
            self.error_lb.setText('Please enter the Author ID Properly')
            self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error\n")
        if insID is not None:
                try:
                    ncur.execute('select author_id from author where author_id='+insID)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Author ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Author ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
        if insID is not None and flag:
                self.error_lb.setText('')
                self.res_le.setText('Result:'+'\n')

                try:
                    drop="EXEC sp_msforeachtable \"ALTER TABLE ? NOCHECK CONSTRAINT all\""
                    activate="exec sp_msforeachtable \"ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all\""
                    U='delete from author where author_id='+insID
                    ncur.execute(drop)
                    ncur.execute(U)
                    ncur.commit()
                    ncur.execute(activate)
                    ncur.commit()
                    self.res_le.setText(str(self.res_le.toPlainText())+"Your Request Has \n Been Executed Successfully\n")
                except:
                    self.res_le.setText(str(self.res_le.toPlainText())+"Fatal Error: Check Your Inputed ID")

