from PyQt4 import QtGui
import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QSplitter, QLabel, QVBoxLayout
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from staff import *
from granter import *
from Book import *
from Author import *
from Member import *
from Publisher import *
from Branch import *
from slide import *
import utils
import sys

import pypyodbc
global connection_string
global c
global cur
connection_string ='Driver={SQL Server};Server=T2SOHEIL\T2SOHEIL;Database=LIBRARY;Uid=sa;Pwd=soheil9759865;'
c = pypyodbc.connect(connection_string)
cur=c.cursor()


class WIDGET(QtGui.QWidget):

    def __init__(self,layout):
        super(WIDGET, self).__init__()
        self.layout=layout
        self.initUI()
    def initUI(self):
        self.setLayout(self.layout)
        self.show()


class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowTitle('Login Page')
        self.lb=QtGui.QLabel()
        myPixmap = QtGui.QPixmap('image.jpg')
        myScaledPixmap = myPixmap.scaled(self.lb.size(), Qt.KeepAspectRatio)
        self.lb.setPixmap(myPixmap)
        # base =str(os.path.dirname(os.path.dirname(__file__)))
        # curntPaths = base +'/Library Managment System/images'
        # imgLst = utils.imageFilePaths(curntPaths)
        # self.lb=SlideShowPics(imgLst)
        self.lb_username=QtGui.QLabel('username: ')
        self.lb_pass=QtGui.QLabel('password: ')
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        h1=QtGui.QHBoxLayout()
        h1.addWidget(self.lb_username)
        h1.addWidget(self.textName)
        h2=QtGui.QHBoxLayout()
        h2.addWidget(self.lb_pass)
        h2.addWidget(self.textPass)
        layout.addWidget(self.lb)
        layout.addLayout(h1)
        layout.addLayout(h2)
        layout.addWidget(self.buttonLogin)

        group=QtGui.QGroupBox('Login')
        group.setLayout(layout)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)

    def handleLogin(self):
        cur.execute('select username,pass from login_tb;')
        lst=[]

        for elm in cur.fetchall():
            lst.append( (str(elm[0]), str(elm[1]) ))
        a=str(self.textName.text())
        b=str(self.textPass.text())
        if (a,b) in lst:
                self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Wrong Credintals , Try Again')


class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.initUI()


    def initUI(self):
        #self.grabber=MyWidget()
        #self.setCentralWidget(self.grabber)
        #view = QWebView()
        #view.load(QUrl('over/index.html'))
        #self.setCentralWidget(view)

        self.center()
        #self.setStyle("")

        self.setWindowTitle('Library Management System')
        self.makeMenu()

        self.show()
        #self.makeMenu()
        #self.show()

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to Exit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def makeMenu(self):
        iconExit = QtGui.QIcon('icons/exit.png')
        exitAction = QtGui.QAction(iconExit, '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        iconBorrow = QtGui.QIcon('icons/attach.png')
        BorrowAction = QtGui.QAction(iconBorrow, '&Borrow', self)
        BorrowAction.setShortcut('Ctrl+l')
        BorrowAction.setStatusTip('Borrow a Book')
        BorrowAction.triggered.connect(self.render_borrow_page)

        iconBorrowRet = QtGui.QIcon('icons/attach.png')
        BorrowRetAction = QtGui.QAction(iconBorrowRet, '&Return', self)
        BorrowRetAction.setShortcut('Ctrl+Q')
        BorrowRetAction.setStatusTip('Return a Book')
        BorrowRetAction.triggered.connect(self.render_borrow_return_page)

        iconRegister = QtGui.QIcon('icons/attach.png')
        RegisterBAction = QtGui.QAction(iconRegister, '&Register', self)
        RegisterBAction.setShortcut('Ctrl+R')
        RegisterBAction.setStatusTip('Register New Book')
        RegisterBAction.triggered.connect(self.render_book_page)

        iconStaff = QtGui.QIcon('icons/attach.png')
        StaffRAction = QtGui.QAction(iconRegister, '&Register', self)
        StaffRAction.setShortcut('Ctrl+P')
        StaffRAction.setStatusTip('Register Staff')
        StaffRAction.triggered.connect(self.render_staff_page)

        iconStaff = QtGui.QIcon('icons/attach.png')
        StaffAAction = QtGui.QAction(iconRegister, '&Absence', self)
        StaffAAction.setShortcut('Ctrl+o')
        StaffAAction.setStatusTip('Register Staff')
        StaffAAction.triggered.connect(self.render_absence_page)

        iconGranterRAction= QtGui.QIcon('icons/attach.png')
        GranterRAction = QtGui.QAction(iconGranterRAction, '&Grants', self)
        GranterRAction.setShortcut('Ctrl+y')
        GranterRAction.setStatusTip('Register Granter')
        GranterRAction.triggered.connect(self.render_granter_reg_page)

        iconAuthReg= QtGui.QIcon('icons/attach.png')
        AuthReg = QtGui.QAction(iconAuthReg, '&Inscribe', self)
        AuthReg.setShortcut('Ctrl+M')
        AuthReg.setStatusTip('Register Author')
        AuthReg.triggered.connect(self.render_auth_reg_page)

        iconAuthCompile= QtGui.QIcon('icons/attach.png')
        AuthCompile = QtGui.QAction(iconAuthCompile, '&Compile', self)
        AuthCompile.setShortcut('Ctrl+C')
        AuthCompile.setStatusTip('Compile Book')
        AuthCompile.triggered.connect(self.render_auth_comp_page)

        iconMemReg= QtGui.QIcon('icons/attach.png')
        MemberRegAction = QtGui.QAction(iconMemReg, '&Register', self)
        MemberRegAction.setShortcut('Ctrl+W')
        MemberRegAction.setStatusTip('Register Member')
        MemberRegAction.triggered.connect(self.render_mem_reg_page)

        iconMemPenalty= QtGui.QIcon('icons/attach.png')
        MemberPenaltyAction = QtGui.QAction(iconMemPenalty, '&Penalty', self)
        MemberPenaltyAction.setShortcut('Ctrl+W')
        MemberPenaltyAction.setStatusTip('Cancel or Check Penalty')
        MemberPenaltyAction.triggered.connect(self.render_mem_penalty_page)

        iconPubReg= QtGui.QIcon('icons/attach.png')
        PubRegAction = QtGui.QAction(iconPubReg, '&Register', self)
        PubRegAction.setShortcut('Ctrl+B')
        PubRegAction.setStatusTip('Register a Publisher')
        PubRegAction.triggered.connect(self.render_pub_reg_page)

        iconBranchReg= QtGui.QIcon('icons/attach.png')
        BranchRegAction = QtGui.QAction(iconBranchReg, '&Register', self)
        BranchRegAction.setShortcut('Ctrl+L')
        BranchRegAction.setStatusTip('Register a Branch')
        BranchRegAction.triggered.connect(self.render_branch_reg_page)

        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        #menubar.setFixedHeight(22)
        menufile = menubar.addMenu('File')
        menuBook=menubar.addMenu('Book' )
        menustaff=menubar.addMenu('Staff')
        menugranter=menubar.addMenu('Grant')
        menuAuth=menubar.addMenu('Author')
        menuMem=menubar.addMenu('Member')
        menuPub=menubar.addMenu('Publisher')
        menuBranch=menubar.addMenu('Branch')
        menuBranch.addAction(BranchRegAction)
        menuPub.addAction(PubRegAction)
        menuMem.addAction(MemberRegAction)
        menuMem.addAction(MemberPenaltyAction)
        menuAuth.addAction(AuthReg)
        menuAuth.addAction(AuthCompile)
        menugranter.addAction(GranterRAction)
        menustaff.addAction(StaffRAction)
        menustaff.addAction(StaffAAction)


        menuBook.addAction(RegisterBAction)
        menuBook.addAction(BorrowAction)
        menuBook.addAction(BorrowRetAction)
        menufile.addAction(exitAction)
    def render_staff_page(self):
        self.ins=StaffReg()
        self.ins.show()
    def render_absence_page(self):
        self.ins_abs=StaffAbsence()
        self.ins_abs.show()
    def render_book_page(self):
        self.d=BookReg()
        self.d.show()
    def render_granter_reg_page(self):
        self.p=GranterReg()
        self.p.show()
    def render_borrow_page(self):
        self.k=BookBorrow()
        self.k.show()
    def render_borrow_return_page(self):
        self.isad=BookRetBorrow()
        self.isad.show()
    def render_auth_reg_page(self):
        self.sds=AuthorRegister()
        self.sds.show()
    def render_auth_comp_page(self):
        self.sd=Compile()
        self.sd.show()
    def render_mem_reg_page(self):
        self.sp=MemberReg()
        self.sp.show()
    def render_mem_penalty_page(self):
        self.pn=Penalty()
        self.pn.show()
    def render_pub_reg_page(self):
        self.pb=PublisherReg()
        self.pb.show()
    def render_branch_reg_page(self):
        self.br=BranchReg()
        self.br.show()
def main():
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks')) #them
    app = QtGui.QApplication(sys.argv)
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QtGui.QIcon('icons/cr2.png'))
    loginDialog = Login()
    if loginDialog.exec_()==QtGui.QDialog.Accepted:
            ex = Main()
            ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
