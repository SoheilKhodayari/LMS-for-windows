__author__ = 'soheil'
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from SaCursor import cur as ncur
from table import BranchTable
class BranchReg(QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BranchReg, self).__init__(parent)
        self.initUI()
        # self.setMinimumWidth(400)
        # self.setMinimumHeight(400)
        self.cur=cur
        self.type=type
        self.setWindowTitle("Branch Registration")
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Done',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.branch_id_le=QtGui.QLineEdit()
        self.head_id_le=QtGui.QLineEdit()
        self.name_le=QtGui.QLineEdit()
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
        self.Fax_le=QtGui.QLineEdit()
        self.Fax_le.setPlaceholderText("Separated by Space")
        self.Website_le=QtGui.QLineEdit()
        self.Website_le.setPlaceholderText("Separated by Space")
        self.errors=QtGui.QLabel(self)




        self.branch_id_lb=QtGui.QPushButton('Branch ID',self)
        self.head_id_lb=QtGui.QPushButton('Head ID',self)
        self.name_lb=QtGui.QPushButton('Name',self)
        self.city_lb=QtGui.QPushButton('City',self)
        self.district_lb=QtGui.QPushButton('District',self)
        self.street_lb=QtGui.QPushButton('Street',self)
        self.alley_lb=QtGui.QPushButton('Alley',self)
        self.building_no_lb = QtGui.QPushButton('Building No',self)
        self.postal_code_lb=QtGui.QPushButton('Postal Code',self)
        self.phone_lb=QtGui.QPushButton('Phone',self)
        self.email_lb=QtGui.QPushButton('Email',self)
        self.Fax_lb=QtGui.QPushButton('Fax',self)
        self.Website_lb=QtGui.QPushButton('Website',self)

        # self.birthdate_ssc_lb = QtGui.QCalendarWidget(self)
        # self.birthdate_ssc_lb.setGridVisible(True)
        # self.birthdate_ssc_lb.clicked[QtCore.QDate].connect(self.setBirth)



        #ADDRESS
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
        self.h1.addWidget(self.branch_id_lb)
        self.h1.addWidget(self.branch_id_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.name_lb)
        self.h2.addWidget(self.name_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.head_id_lb)
        self.h3.addWidget(self.head_id_le)

        self.hss1=QtGui.QHBoxLayout()
        self.hss1.addWidget(self.phone_lb)
        self.hss1.addWidget(self.phone_le)
        self.hss2=QtGui.QHBoxLayout()
        self.hss2.addWidget(self.email_lb)
        self.hss2.addWidget(self.email_le)
        self.hss3=QtGui.QHBoxLayout()
        self.hss3.addWidget(self.Fax_lb)
        self.hss3.addWidget(self.Fax_le)
        self.hss4=QtGui.QHBoxLayout()
        self.hss4.addWidget(self.Website_lb)
        self.hss4.addWidget(self.Website_le)




        self.basic=QtGui.QVBoxLayout()
        self.basic.addLayout(self.h1)
        self.basic.addLayout(self.h2)
        self.basic.addLayout(self.h3)
        self.basic.addLayout(self.hss1)
        self.basic.addLayout(self.hss2)
        self.basic.addLayout(self.hss3)
        self.basic.addLayout(self.hss4)


        self.addr=QtGui.QVBoxLayout()
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

        group=QtGui.QGroupBox('Branch Registration')
        group.setLayout(vb)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        Comma=','
        try :
            branchID=str(self.branch_id_le.text())
            name=str(self.name_le.text())
            head_id=str(self.head_id_le.text())
            city=str(self.city_le.text())
            district=str(self.district_le.text())
            street=str(self.street_le.text())
            alley=str(self.alley_le.text())
            building_no=str(self.building_no_le.text())
            postal_code=str(self.postal_code_le.text())
            print 'BranchInsert '+branchID+Comma+name+Comma+head_id+Comma+city+Comma+district+Comma+street+Comma+alley+Comma+building_no+Comma+postal_code
            ncur.execute('EXEC BranchInsert '+branchID+Comma+name+Comma+head_id+Comma+city+Comma+district+Comma+street+Comma+alley+Comma+building_no+Comma+postal_code+';Commit;')

            phones=str(self.phone_le.text()).split()
            faxes=str(self.Fax_le.text()).split()
            websites=str(self.Website_le.text()).split()
            emails=str(self.email_le.text()).split()
            for phone in phones:
                 ncur.execute('EXEC BranchPhoneInsert '+branchID+Comma+'\"' +phone +'\"' +';Commit;')
            for fax in faxes:
                 ncur.execute('EXEC BranchFaxInsert '+branchID+Comma+'\"' +fax+'\"'+';Commit;')
            for wbs in websites:
                 #print 'EXEC BranchWebsiteInsert '+branchID+Comma+'\"'+wbs+'\"'+';Commit;'
                 ncur.execute('EXEC BranchWebsiteInsert '+branchID+Comma+'\"'+wbs+'\"'+';Commit;')
            for email in emails:
                 ncur.execute('EXEC BranchEmailInsert '+branchID+Comma+'\"'+email+'\"'+';Commit;')

            print 'successfully inserted'
            self.close()

        except :
            self.errors.setText("There are some errors in your inserted fields, fix them and then try again")


class BranchSearch(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BranchSearch, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.setWindowTitle('Branch Search')
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
        self.searchType.addItem("ByName")
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
        elif t=="ByName": self.opcode=2
        elif t=="ByCity": self.opcode=3
        else: self.opcode=0

        field=str(self.searchField_le.text())

        if self.opcode==0:
            try:
                ncur.execute("select * from getBranchList()")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")

        elif self.opcode==1:
            try:
                ncur.execute("select * from getBranchById("+field+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==2:
            try:
                ncur.execute("select * from getBranchListByName("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")
        elif self.opcode==3:
            try:
                ncur.execute("select * from getBranchListByCity("+"\'"+field+"\'"+")")
                self.data=ncur.fetchall()
            except:
                self.lbl.setText("               No results were found, Please Search a More Precise Value.")


        if len(self.data)!=0:
            if self.Btb is None:
                self.lbl.setText("")
                self.Btb=BranchTable(self.data)
            else:
                self.lbl.setText("")
                self.Btb.setParent(None)
                self.Btb=BranchTable(self.data)



            self.Vbox.addWidget(self.Btb)
        else:
             self.lbl.setText("               No results were found, Please Search a More Precise Value.")
             print 'no results were found'


    def onActivated(self,text):
        self.searchType_le.setText(text)


class BranchContact(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BranchContact, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Branch Contact')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Branch ID:')
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
        cont_dict['faxList']=''
        cont_dict['websiteList']=''

        bid=str(self.id_le.text())


        if bid=='':
            bid=None
            self.error_lb.setText('Please enter the Branch ID Properly')
            self.contact_le.setText('')
        if bid is not None:
                try:
                    ncur.execute('select branch_id from Branch where branch_id='+bid)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Branch ID')
                    self.contact_le.setText('')
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Branch ID')
                    self.contact_le.setText('')



        if bid is not None and flag:
                self.error_lb.setText('')

                ncur.execute('select * from Branch_email where branch_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['mailList']+='    '+elm[1]+'\n'


                ncur.execute('select * from Branch_phone where branch_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['phoneList']+='    '+elm[1]+'\n'


                ncur.execute('select * from Branch_fax where branch_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['faxList']+='    '+elm[1]+'\n'


                ncur.execute('select * from Branch_website where branch_id='+bid)
                for elm in ncur.fetchall():
                    cont_dict['websiteList']+='    '+elm[1]+'\n'

                text='Phones: \n' + cont_dict['phoneList'] + '\n' \
                     'Mails: \n' + cont_dict['mailList'] + '\n' \
                     'Faxes: \n' + cont_dict['faxList'] + '\n'  \
                     'Websites: \n' + cont_dict['websiteList'] + '\n'


                self.contact_le.setText(text)


class BranchDelete(QtGui.QWidget):
    def __init__( self,cur,type, parent=None  ):
        super(BranchDelete, self).__init__(parent)
        self.cur=cur
        self.type=type
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Branch Deletion')
        self.error_lb=QtGui.QLabel()
        self.id_lb=QtGui.QLabel('Branch ID:')
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
            self.error_lb.setText('Please enter the Branch ID Properly')
            self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error\n")
        if insID is not None:
                try:
                    ncur.execute('select branch_id from branch where branch_id='+insID)
                except:
                    flag=False
                    self.error_lb.setText('Please enter a valid Branch ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
                m=ncur.fetchall()
                print m
                if len(m)==0:
                    flag=False
                    self.error_lb.setText('Please enter a valid Branch ID')
                    self.res_le.setText('Result:'+'\n'+"No Operation Done Due to A Previous Error")
        if insID is not None and flag:
                self.error_lb.setText('')
                self.res_le.setText('Result:'+'\n')

                try:
                    drop="EXEC sp_msforeachtable \"ALTER TABLE ? NOCHECK CONSTRAINT all\""
                    activate="exec sp_msforeachtable \"ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all\""
                    U='delete from branch where branch_id='+insID
                    ncur.execute(drop)
                    ncur.execute(U)
                    ncur.commit()
                    ncur.execute(activate)
                    ncur.commit()
                    self.res_le.setText(str(self.res_le.toPlainText())+"Your Request Has \n Been Executed Successfully\n")
                except:
                    self.res_le.setText(str(self.res_le.toPlainText())+"Fatal Error: Check Your Inputed ID")
















