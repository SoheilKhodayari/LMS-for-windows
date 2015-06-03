__author__ = 'soheil'
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *

class BranchReg(QWidget):
    def __init__( self, parent=None  ):
        super(BranchReg, self).__init__(parent)
        self.initUI()
        # self.setMinimumWidth(400)
        # self.setMinimumHeight(400)
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
        pass
