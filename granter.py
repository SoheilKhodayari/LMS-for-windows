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
from table import GranterTable
import sys
from SaCursor import cur as ncur
class GranterReg(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(GranterReg, self).__init__(parent)
        self.initUI()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.setWindowTitle("Granter")
        self.cur=cur
        self.type=type
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Done',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.granter_id_le=QtGui.QLineEdit()
        self.fname_le=QtGui.QLineEdit()
        self.lname_le=QtGui.QLineEdit()
        self.ssn_le=QtGui.QLineEdit()
        self.country_le=QtGui.QLineEdit()
        self.city_le=QtGui.QLineEdit()
        self.district_le=QtGui.QLineEdit()
        self.street_le=QtGui.QLineEdit()
        self.alley_le=QtGui.QLineEdit()
        self.building_no_le = QtGui.QLineEdit()
        self.postal_code_le=QtGui.QLineEdit()
        self.phone_le=QtGui.QLineEdit()
        self.phone_le.setPlaceholderText("Separated by Space")
        self.email_le=QtGui.QLineEdit()
        self.email_le.setPlaceholderText("Separated by Space")
        self.serial_ssc_le=QtGui.QLineEdit()
        self.issuancelocation_ssc_le=QtGui.QLineEdit()
        self.birthdate_ssc_le=QtGui.QDateEdit()
        self.errors=QtGui.QLabel(self)




        self.granter_id_lb=QtGui.QPushButton('Granter ID',self)
        self.fname_lb=QtGui.QPushButton('First Name',self)
        self.lname_lb=QtGui.QPushButton('Last Name',self)
        self.ssn_lb=QtGui.QPushButton('SSN',self)
        self.country_lb=QtGui.QPushButton('Country',self)
        self.city_lb=QtGui.QPushButton('City',self)
        self.district_lb=QtGui.QPushButton('District',self)
        self.street_lb=QtGui.QPushButton('Street',self)
        self.alley_lb=QtGui.QPushButton('Alley',self)
        self.building_no_lb = QtGui.QPushButton('Building No',self)
        self.postal_code_lb=QtGui.QPushButton('Postal Code',self)
        self.phone_lb=QtGui.QPushButton('Phone',self)
        self.email_lb=QtGui.QPushButton('Email',self)
        self.serial_ssc_lb=QtGui.QPushButton("Serial",self)
        self.issuancelocation_ssc_lb=QtGui.QPushButton("ISL",self)
        self.birthdate_ssc_lb=QtGui.QPushButton("Birth Date",self)
        # self.birthdate_ssc_lb = QtGui.QCalendarWidget(self)
        # self.birthdate_ssc_lb.setGridVisible(True)
        # self.birthdate_ssc_lb.clicked[QtCore.QDate].connect(self.setBirth)



        #CONTACT
        self.hss=QtGui.QHBoxLayout()
        self.hss.addWidget(self.phone_lb)
        self.hss.addWidget(self.phone_le)
        self.hss.addWidget(self.email_lb)
        self.hss.addWidget(self.email_le)
        #ADDRESS
        self.hdd=QtGui.QHBoxLayout()
        self.hdd.addWidget(self.country_lb)
        self.hdd.addWidget(self.country_le)
        self.h8=QtGui.QHBoxLayout()
        self.h8.addWidget(self.city_lb)
        self.h8.addWidget(self.city_le)
        self.h9=QtGui.QHBoxLayout()
        self.h9.addWidget(self.district_lb)
        self.h9.addWidget(self.district_le)
        self.h10=QtGui.QHBoxLayout()
        self.h10.addWidget(self.street_lb)
        self.h10.addWidget(self.street_le)
        self.h11=QtGui.QHBoxLayout()
        self.h11.addWidget(self.alley_lb)
        self.h11.addWidget(self.alley_le)
        self.h12=QtGui.QHBoxLayout()
        self.h12.addWidget(self.building_no_lb)
        self.h12.addWidget(self.building_no_le)
        self.h13=QtGui.QHBoxLayout()
        self.h13.addWidget(self.postal_code_lb)
        self.h13.addWidget(self.postal_code_le)

        #DONE BTN
        self.h14=QtGui.QHBoxLayout()
        self.h14.addWidget(self.btn_done)

        #Basic INFO
        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.granter_id_lb)
        self.h1.addWidget(self.granter_id_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.fname_lb)
        self.h2.addWidget(self.fname_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.lname_lb)
        self.h3.addWidget(self.lname_le)
        self.h7=QtGui.QHBoxLayout()
        self.h7.addWidget(self.ssn_lb)
        self.h7.addWidget(self.ssn_le)
        self.ssc1=QtGui.QHBoxLayout()
        self.ssc1.addWidget(self.serial_ssc_lb)
        self.ssc1.addWidget(self.serial_ssc_le)
        self.ssc2=QtGui.QHBoxLayout()
        self.ssc2.addWidget(self.issuancelocation_ssc_lb)
        self.ssc2.addWidget(self.issuancelocation_ssc_le)
        self.ssc3=QtGui.QHBoxLayout()
        self.ssc3.addWidget(self.birthdate_ssc_lb)
        self.ssc3.addWidget(self.birthdate_ssc_le)



        self.basic=QtGui.QVBoxLayout()
        self.basic.addLayout(self.h1)
        self.basic.addLayout(self.h2)
        self.basic.addLayout(self.h3)
        self.basic.addLayout(self.h7)
        self.basic.addLayout(self.ssc1)
        self.basic.addLayout(self.ssc2)
        self.basic.addLayout(self.ssc3)



        self.contact=QtGui.QVBoxLayout()
        self.contact.addLayout(self.hss)
        # self.contact.addLayout(self.hss1)
        # self.contact.addLayout(self.hss2)
        # self.contact.addLayout(self.hdd1)
        # self.contact.addLayout(self.hdd2)

        self.addr=QtGui.QVBoxLayout()
        self.addr.addLayout(self.hdd)
        self.addr.addLayout(self.h8)
        self.addr.addLayout(self.h9)
        self.addr.addLayout(self.h10)
        self.addr.addLayout(self.h11)
        self.addr.addLayout(self.h12)
        self.addr.addLayout(self.h13)




        group1=QtGui.QGroupBox('Basic Info')
        group1.setLayout(self.basic)
        group2=QtGui.QGroupBox('Contact')
        group2.setLayout(self.contact)
        group3=QtGui.QGroupBox('Address')
        group3.setLayout(self.addr)

        hb1=QtGui.QHBoxLayout()
        hb1.addWidget(group1)
        hb1.addWidget(group3)
        hb2=QtGui.QHBoxLayout()
        hb2.addWidget(group2)
        hb3=QtGui.QHBoxLayout()
        hb3.addWidget(self.errors)
        vb=QtGui.QVBoxLayout()
        vb.addLayout(hb1)
        vb.addLayout(hb2)
        vb.addLayout(hb3)
        vb.addLayout(self.h14)

        group=QtGui.QGroupBox('')
        group.setLayout(vb)
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
        Comma=','
        try:
            GID=str(self.granter_id_le.text())
            fname=str(self.fname_le.text())
            lname=str(self.lname_le.text())
            ssn=str(self.ssn_le.text())
            serial=str(self.serial_ssc_le.text())
            ISL=str(self.issuancelocation_ssc_le.text())
            birthDate=self.convertDate(str(self.birthdate_ssc_le.text()))
            country=str(self.country_le.text())
            city=str(self.city_le.text())
            district=str(self.district_le.text())
            street=str(self.street_le.text())
            alley=str(self.alley_le.text())
            bulidingNo=str(self.building_no_le.text())
            postalCode=str(self.postal_code_le.text())
            phones=str(self.phone_le.text()).split()
            emails=str(self.email_le.text()).split()

            ncur.execute('EXEC GranterInsert '+GID+Comma+fname+Comma+lname+Comma+ssn+Comma+'\''+serial+'\''+Comma+ISL+Comma+'\''+birthDate+'\''+Comma+country+Comma+city+Comma+district+Comma+street+Comma+alley+Comma+bulidingNo+Comma+postalCode+';Commit;')
            print 'successfully inserted Granter'

            for phone in phones:
                 ncur.execute('EXEC GranterPhoneInsert '+GID+Comma+'\"' +phone +'\"' +';Commit;')
            for email in emails:
                 ncur.execute('EXEC GranterEmailInsert '+GID+Comma+'\"'+email+'\"'+';Commit;')
            print 'successfully inserted Phones,Emails'
            self.close()

        except:
            self.errors.setText("There are some errors in your inserted fields, fix them and then try again")


class GranterSearch(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(GranterSearch, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.setWindowTitle('Granter Search')
        self.initUI()
    def initUI(self):
        self.Btb=None
        self.data=None
        self.searchType_le=QtGui.QLineEdit()
        self.searchType_le.setReadOnly(True)
        self.searchField_le=QtGui.QLineEdit()
        self.searchField_le.setPlaceholderText('')
        self.searchField_lb=QtGui.QPushButton('SearchField',self)
        self.searchType = QtGui.QComboBox(self)
        self.searchType.setFixedSize(75,23)
        self.searchType.addItem("FullList")
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

        self.group=QtGui.QGroupBox('Branch Search')
        self.group.setLayout(self.v)
        self.Vbox=QtGui.QVBoxLayout()
        self.Vbox.addLayout(hds)
        self.Vbox.addWidget(self.group)

        self.setLayout(self.Vbox)




    def executeAction(self):
        self.lbl.setText("")
        self.opcode=None
        t=str(self.searchType_le.text())
        if t=="FullList": self.opcode=0
        elif t=="ByID": self.opcode=1
        elif t=="ByFname": self.opcode=2
        elif t=="ByLname": self.opcode=3
        else: self.opcode=0

        field=str(self.searchField_le.text())

        if self.opcode==0:
            try:
                ncur.execute("select * from getGranterList()")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        elif self.opcode==1:
            try:
                ncur.execute("select * from getGranterById("+field+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==2:
            try:
                ncur.execute("select * from getGranterListByFName("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==3:
            try:
                ncur.execute("select * from getGranterListBylName("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")


        if len(self.data)!=0:
            if self.Btb is None:
                self.lbl.setText("")
                self.Btb=GranterTable(self.data)
            else:
                self.lbl.setText("")
                self.Btb.setParent(None)
                if self.opcode!=3:
                    self.Btb=GranterTable(self.data)
                else:
                    self.Btb=GranterTable(self.data)

            self.Vbox.addWidget(self.Btb)
        else:
             self.lbl.setText("               No results were found, Please Search a More Precise Value.")
             print 'no results were found'


    def onActivated(self,text):
        self.searchType_le.setText(text)


class GranterContact(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(GranterContact, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Granter Contact')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Granter ID:')
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
            self.error_lb.setText('Please enter the Branch ID Properly')
            self.contact_le.setText('')
        if bid is not None:
                try:
                    ncur.execute('select granter_id from granter where granter_id='+bid)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Granter ID')
                    self.contact_le.setText('')
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Granter ID')
                    self.contact_le.setText('')



        if bid is not None and flag:
                self.error_lb.setText('')

                ncur.execute('select * from granter_email where granter_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['mailList']+='    '+elm[1]+'\n'


                ncur.execute('select * from granter_phone where granter_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['phoneList']+='    '+elm[1]+'\n'



                text='Phones: \n' + cont_dict['phoneList'] + '\n' \
                     'Mails: \n' + cont_dict['mailList']



                self.contact_le.setText(text)

class GranterDelete(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(GranterDelete, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Granter Deletion')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Granter ID:')
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
            self.error_lb.setText('Please enter the Granter ID Properly')
            self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error\n")
        if insID is not None:
                try:
                    ncur.execute('select granter_id from granter where granter_id='+insID)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Granter ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Granter ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
        if insID is not None and flag:
                self.error_lb.setText('')
                self.res_le.setText('Result:'+'\n')

                try:
                    drop="EXEC sp_msforeachtable \"ALTER TABLE ? NOCHECK CONSTRAINT all\""
                    activate="exec sp_msforeachtable \"ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all\""
                    U='delete from granter where granter_id='+insID
                    ncur.execute(drop)
                    ncur.execute(U)
                    ncur.commit()
                    ncur.execute(activate)
                    ncur.commit()
                    self.res_le.setText(str(self.res_le.toPlainText())+"Your Request Has \n Been Executed Successfully\n")
                except:
                    self.res_le.setText(str(self.res_le.toPlainText())+"Fatal Error: Check Your Inputed ID")



