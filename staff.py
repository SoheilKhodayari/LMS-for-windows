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


#Staff Lists
# data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
#
# class MyTable(QTableWidget):
#     def __init__(self, data, *args):
#         QTableWidget.__init__(self, *args)
#         self.data = data
#         self.setmydata()
#         self.resizeColumnsToContents()
#         self.resizeRowsToContents()
#
#     def setmydata(self):
#
#         horHeaders = []
#         for n, key in enumerate(sorted(self.data.keys())):
#             horHeaders.append(key)
#             for m, item in enumerate(self.data[key]):
#                 newitem = QTableWidgetItem(item)
#                 self.setItem(m, n, newitem)
#         self.setHorizontalHeaderLabels(horHeaders)
class StaffReg(QWidget):
    def __init__( self, parent=None  ):
        super(StaffReg, self).__init__(parent)
        self.initUI()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.setWindowTitle("Staff Registration")
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Done',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.staff_id_le=QtGui.QLineEdit()
        self.fname_le=QtGui.QLineEdit()
        self.lname_le=QtGui.QLineEdit()
        self.branch_id_le=QtGui.QLineEdit()
        self.salary_le=QtGui.QLineEdit()
        self.employed_date_le=QtGui.QDateEdit()
        self.ssn_le=QtGui.QLineEdit()
        self.city_le=QtGui.QLineEdit()
        self.district_le=QtGui.QLineEdit()
        self.street_le=QtGui.QLineEdit()
        self.alley_le=QtGui.QLineEdit()
        self.building_no_le = QtGui.QLineEdit()
        self.postal_code_le=QtGui.QLineEdit()
        self.phone_le=QtGui.QLineEdit()
        self.phone_le.setPlaceholderText("Separate Phone Numbers by Space")
        self.extraPhone_le=QtGui.QLineEdit()
        self.email_le=QtGui.QLineEdit()
        self.email_le.setPlaceholderText("Separate Emails by Space")
        self.extraEmail_le=QtGui.QLineEdit()
        self.serial_ssc_le=QtGui.QLineEdit()
        self.issuancelocation_ssc_le=QtGui.QLineEdit()
        self.birthdate_ssc_le=QtGui.QDateEdit()



        self.staff_id_lb=QtGui.QPushButton('ID',self)
        self.fname_lb=QtGui.QPushButton('First Name',self)
        self.lname_lb=QtGui.QPushButton('Last Name',self)
        self.branch_id_lb=QtGui.QPushButton('BranchID',self)
        self.salary_lb=QtGui.QPushButton('Salary',self)
        self.employed_date_lb=QtGui.QPushButton('Date Employed',self)
        self.ssn_lb=QtGui.QPushButton('SSN',self)
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


        #Occupation
        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.staff_id_lb)
        self.h1.addWidget(self.staff_id_le)
        self.h4=QtGui.QHBoxLayout()
        self.h4.addWidget(self.branch_id_lb)
        self.h4.addWidget(self.branch_id_le)
        self.h5=QtGui.QHBoxLayout()
        self.h5.addWidget(self.salary_lb)
        self.h5.addWidget(self.salary_le)
        self.h6=QtGui.QHBoxLayout()
        self.h6.addWidget(self.employed_date_lb)
        self.h6.addWidget(self.employed_date_le)

        #CONTACT
        self.hss1=QtGui.QHBoxLayout()
        self.hss1.addWidget(self.phone_lb)
        self.hss1.addWidget(self.phone_le)
        self.hss2=QtGui.QHBoxLayout()
        self.hss2.addWidget(self.extraPhone_le)
        self.hdd1=QtGui.QHBoxLayout()
        self.hdd1.addWidget(self.email_lb)
        self.hdd1.addWidget(self.email_le)
        self.hdd2=QtGui.QHBoxLayout()
        self.hdd2.addWidget(self.extraEmail_le)
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
        self.basic.addLayout(self.h2)
        self.basic.addLayout(self.h3)
        self.basic.addLayout(self.h7)
        self.basic.addLayout(self.ssc1)
        self.basic.addLayout(self.ssc2)
        self.basic.addLayout(self.ssc3)

        self.occupation=QtGui.QVBoxLayout()
        self.occupation.addLayout(self.h1)
        self.occupation.addLayout(self.h4)
        self.occupation.addLayout(self.h5)
        self.occupation.addLayout(self.h6)

        self.contact=QtGui.QVBoxLayout()
        self.contact.addLayout(self.hss1)
        self.contact.addLayout(self.hss2)
        self.contact.addLayout(self.hdd1)
        self.contact.addLayout(self.hdd2)

        self.addr=QtGui.QVBoxLayout()
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
        group4=QtGui.QGroupBox('Occupation')
        group4.setLayout(self.occupation)

        hb1=QtGui.QHBoxLayout()
        hb1.addWidget(group1)
        hb1.addWidget(group3)
        hb2=QtGui.QHBoxLayout()
        hb2.addWidget(group4)
        hb2.addWidget(group2)
        vb=QtGui.QVBoxLayout()
        vb.addLayout(hb1)
        vb.addLayout(hb2)
        vb.addLayout(self.h14)

        group=QtGui.QGroupBox('')
        group.setLayout(vb)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass
    # def setBirth(self,date):
    #     self.birthdate_ssc_le.setText(str(date))

class StaffAbsence(QWidget):
    def __init__( self, parent=None  ):
        super(StaffAbsence, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.btn_done=QtGui.QPushButton('Inscribe',self)
        self.btn_done.resize(self.btn_done.sizeHint())
        self.connect(self.btn_done, QtCore.SIGNAL("clicked()"),self.done)

        self.staff_id_le=QtGui.QLineEdit()
        self.absence_date_le=QtGui.QDateEdit()


        self.staff_id_lb=QtGui.QPushButton('ID',self)
        self.absence_date_lb=QtGui.QPushButton('Absence Date',self)



        self.h1=QtGui.QHBoxLayout()
        self.h1.addWidget(self.staff_id_lb)
        self.h1.addWidget(self.staff_id_le)
        self.h2=QtGui.QHBoxLayout()
        self.h2.addWidget(self.absence_date_lb)
        self.h2.addWidget(self.absence_date_le)
        self.h3=QtGui.QHBoxLayout()
        self.h3.addWidget(self.btn_done)


        self.v1=QtGui.QVBoxLayout()
        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        self.v1.addLayout(self.h3)


        group=QtGui.QGroupBox('Staff Absence')
        group.setLayout(self.v1)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
    def done(self):
        pass