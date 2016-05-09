__author__ = 'soheil'

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
import sys
from table import PublisherTable
from SaCursor import cur as ncur
class PublisherReg(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(PublisherReg, self).__init__(parent)
        self.initUI()
        # self.setMinimumWidth(400)
        # self.setMinimumHeight(400)
        self.setWindowTitle("Publisher Registration")
        self.cur=cur
        self.type=type
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Done',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.pub_id_le=QtGui.QLineEdit()
        self.fname_le=QtGui.QLineEdit()
        #self.lname_le=QtGui.QLineEdit()
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
        self.country_le=QtGui.QLineEdit()
        self.errors=QtGui.QLabel(self)





        self.pub_id_lb=QtGui.QPushButton('Pub ID',self)
        self.fname_lb=QtGui.QPushButton('Name',self)
        #self.lname_lb=QtGui.QPushButton('Last Name',self)
        self.city_lb=QtGui.QPushButton('City',self)
        self.district_lb=QtGui.QPushButton('District',self)
        self.street_lb=QtGui.QPushButton('Street',self)
        self.alley_lb=QtGui.QPushButton('Alley',self)
        self.building_no_lb = QtGui.QPushButton('Building No',self)
        self.postal_code_lb=QtGui.QPushButton('Postal Code',self)
        self.phone_lb=QtGui.QPushButton('Phone',self)
        self.email_lb=QtGui.QPushButton('Email',self)
        self.country_lb=QtGui.QPushButton('Country',self)

        # self.birthdate_ssc_lb = QtGui.QCalendarWidget(self)
        # self.birthdate_ssc_lb.setGridVisible(True)
        # self.birthdate_ssc_lb.clicked[QtCore.QDate].connect(self.setBirth)



        #ADDRESS
        self.dh=QtGui.QHBoxLayout()
        self.dh.addWidget(self.country_lb)
        self.dh.addWidget(self.country_le)
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
        self.h1.addWidget(self.pub_id_lb)
        self.h1.addWidget(self.pub_id_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.fname_lb)
        self.h2.addWidget(self.fname_le)
        # self.h3=QtGui.QHBoxLayout()
        # self.h3.addWidget(self.lname_lb)
        # self.h3.addWidget(self.lname_le)

        self.hss1=QtGui.QHBoxLayout()
        self.hss1.addWidget(self.phone_lb)
        self.hss1.addWidget(self.phone_le)
        self.hss2=QtGui.QHBoxLayout()
        self.hss2.addWidget(self.email_lb)
        self.hss2.addWidget(self.email_le)




        self.basic=QtGui.QVBoxLayout()
        self.basic.addLayout(self.h1)
        self.basic.addLayout(self.h2)
        #self.basic.addLayout(self.h3)
        self.basic.addLayout(self.hss1)
        self.basic.addLayout(self.hss2)


        self.addr=QtGui.QVBoxLayout()
        self.addr.addLayout(self.dh)
        self.addr.addLayout(self.h8)
        self.addr.addLayout(self.h9)
        self.addr.addLayout(self.h10)
        self.addr.addLayout(self.h11)
        self.addr.addLayout(self.h12)
        self.addr.addLayout(self.h13)




        group1=QtGui.QGroupBox('Basic Info')
        group1.setLayout(self.basic)
        group3=QtGui.QGroupBox('Address')
        group3.setLayout(self.addr)

        hb1=QtGui.QHBoxLayout()
        hb1.addWidget(group1)
        hb1.addWidget(group3)
        hb3=QtGui.QHBoxLayout()
        hb3.addWidget(self.errors)
        vb=QtGui.QVBoxLayout()
        vb.addLayout(hb1)
        vb.addLayout(hb3)
        vb.addLayout(self.h14)

        group=QtGui.QGroupBox('Pulisher Registration')
        group.setLayout(vb)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        Comma=','
        try:
            pubID=str(self.pub_id_le.text())
            name=str(self.fname_le.text())
            country=str(self.country_le.text())
            city=str(self.city_le.text())
            district=str(self.district_le.text())
            street=str(self.street_le.text())
            alley=str(self.alley_le.text())
            buildingNo=str(self.building_no_le.text())
            postalCode=str(self.postal_code_le.text())
            phones=str(self.phone_le.text()).split()
            emails=str(self.email_le.text()).split()

            ncur.execute('EXEC PublisherInsert '+pubID+Comma+name+Comma+country+Comma+city+Comma+district
            +Comma+street+Comma+alley+Comma+buildingNo+Comma+postalCode+';Commit;')

            for phone in phones:
                ncur.execute('EXEC PublisherPhoneInsert '+pubID+Comma+'\"' +phone +'\"' +';Commit;')
            for email in emails:

                ncur.execute('EXEC PublihserEmailInsert '+pubID+Comma+'\"'+email+'\"'+';Commit;')

            print 'successfully inserted'
            self.close()
        except:
            self.errors.setText("There are some errors in your inserted fields, fix them and then try again")


class PubSearch(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(PubSearch, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.setWindowTitle('Publisher Search')
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
        self.searchType.addItem("PubList")
        self.searchType.addItem("ByID")
        self.searchType.addItem("ByName")
        self.searchType.addItem("ByCountry")
        self.searchType.addItem("ByCity")
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

        self.group=QtGui.QGroupBox('Publisher Search')
        self.group.setLayout(self.v)
        self.Vbox=QtGui.QVBoxLayout()
        self.Vbox.addLayout(hds)
        self.Vbox.addWidget(self.group)

        self.setLayout(self.Vbox)




    def executeAction(self):
        self.lbl.setText("")
        self.opcode=None
        t=str(self.searchType_le.text())
        if t=="PubList": self.opcode=0
        elif t=="ByID": self.opcode=1
        elif t=="ByName": self.opcode=2
        elif t=="ByCountry": self.opcode=3
        elif t=="ByCity": self.opcode=4
        else: self.opcode=0

        field=str(self.searchField_le.text())

        if self.opcode==0:
            try:
                ncur.execute("select * from getPublisherList()")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        elif self.opcode==1:
            try:
                ncur.execute("select * from getPublisherById("+field+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==2:
            try:
                ncur.execute("select * from getPublisherListByName("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==3:
            try:
                ncur.execute("select * from getPublisherListByCountry("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==4:
            try:
                ncur.execute("select * from getPublisherListByCity("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        if len(self.data)!=0:
            if self.Btb is None:
                self.lbl.setText("")
                self.Btb=PublisherTable(self.data)
            else:
                self.lbl.setText("")
                self.Btb.setParent(None)
                if self.opcode!=3:
                    self.Btb=PublisherTable(self.data)
                else:
                    self.Btb=PublisherTable(self.data)

            self.Vbox.addWidget(self.Btb)
        else:
             self.lbl.setText("               No results were found, Please Search a More Precise Value.")
             print 'no results were found'


    def onActivated(self,text):   #self.combo3.currenttext() also catches its selection
        self.searchType_le.setText(text)


class PubContact(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(PubContact, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Publisher Contact')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Publisher ID:')
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
            self.error_lb.setText('Please enter the Pub ID Properly')
            self.contact_le.setText('')
        if bid is not None:
                try:
                    ncur.execute('select pub_id from publisher where pub_id='+bid)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Pub ID')
                    self.contact_le.setText('')
                m=ncur.fetchall()
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Pub ID')
                    self.contact_le.setText('')



        if bid is not None and flag:
                self.error_lb.setText('')

                ncur.execute('select * from publisher_email where publisher_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['mailList']+='    '+elm[1]+'\n'

                ncur.execute('select * from publisher_phone where publisher_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['phoneList']+='    '+elm[1]+'\n'



                text='Phones: \n' + cont_dict['phoneList'] + '\n' \
                     'Mails: \n' + cont_dict['mailList']



                self.contact_le.setText(text)


class PubDelete(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(PubDelete, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Publisher Deletion')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Publisher ID:')
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
            self.error_lb.setText('Please enter the Pub ID Properly')
            self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error\n")
        if insID is not None:
                try:
                    ncur.execute('select pub_id from publisher where pub_id='+insID)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Pub ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Pub ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
        if insID is not None and flag:
                self.error_lb.setText('')
                self.res_le.setText('Result:'+'\n')

                try:
                    drop="EXEC sp_msforeachtable \"ALTER TABLE ? NOCHECK CONSTRAINT all\""
                    activate="exec sp_msforeachtable \"ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all\""
                    U='delete from publisher where pub_id='+insID
                    ncur.execute(drop)
                    ncur.execute(U)
                    ncur.commit()
                    ncur.execute(activate)
                    ncur.commit()
                    self.res_le.setText(str(self.res_le.toPlainText())+"Your Request Has \n Been Executed Successfully\n")
                except:
                    self.res_le.setText(str(self.res_le.toPlainText())+"Fatal Error: Check Your Inputed ID")



