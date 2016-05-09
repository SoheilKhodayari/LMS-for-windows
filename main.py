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
from table import *
import pypyodbc
from mainUI import MyTable
from SaCursor import *



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
                self.nType,self.ncur=changeConnection(a)
                print 'connection changed to user:'+a+" of type "+str(self.nType)

                self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Wrong Credintals , Try Again')



class Main(QtGui.QMainWindow):
    def __init__(self,cur,type):
        super(Main, self).__init__()
        # self.setMinimumWidth(600)
        # self.setMinimumHeight(600)
        self.setMinimumWidth(600)
        self.setMinimumWidth(600)
        self.cur=cur
        self.type=type
        self.initUI()



    def initUI(self):

        self.center()
        self.setWindowTitle('Library Management System')
        self.widget=MyTable(self.cur,self.type)
        self.setCentralWidget(self.widget)

        self.makeMenu()
        self.show()


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

        iconBorrow = QtGui.QIcon('icons/borrow.png')
        BorrowAction = QtGui.QAction(iconBorrow, '&Borrow', self)
        BorrowAction.setShortcut('Ctrl+l')
        BorrowAction.setStatusTip('Borrow a Book')
        BorrowAction.triggered.connect(self.render_borrow_page)

        iconBorrowRet = QtGui.QIcon('icons/text.png')
        BorrowRetAction = QtGui.QAction(iconBorrowRet, '&Return', self)
        BorrowRetAction.setShortcut('Ctrl+Q')
        BorrowRetAction.setStatusTip('Return a Book')
        BorrowRetAction.triggered.connect(self.render_borrow_return_page)

        iconRegister = QtGui.QIcon('icons/register.png')
        RegisterBAction = QtGui.QAction(iconRegister, '&Register', self)
        RegisterBAction.setShortcut('Ctrl+R')
        RegisterBAction.setStatusTip('Register New Book')
        RegisterBAction.triggered.connect(self.render_book_page)

        iconStaff = QtGui.QIcon('icons/add3.png')
        StaffRAction = QtGui.QAction(iconStaff, '&Register', self)
        StaffRAction.setShortcut('Ctrl+P')
        StaffRAction.setStatusTip('Register Staff')
        StaffRAction.triggered.connect(self.render_staff_page)

        iconStaffh = QtGui.QIcon('icons/add2.png')
        StaffAAction = QtGui.QAction(iconStaffh, '&Absence Addition', self)
        StaffAAction.setShortcut('Ctrl+o')
        StaffAAction.setStatusTip('Register Staff')
        StaffAAction.triggered.connect(self.render_absence_page)

        iconStaffAB = QtGui.QIcon('icons/size.png')
        StaffAReportAction = QtGui.QAction(iconStaffAB, '&Absence Reports', self)
        StaffAReportAction.setShortcut('Ctrl+A')
        StaffAReportAction.setStatusTip('Absence Reports')
        StaffAReportAction.triggered.connect(self.render_absence_report_page)

        iconStaffSearch = QtGui.QIcon('icons/search.png')
        StaffSearchAction = QtGui.QAction(iconStaffSearch, '&Search', self)
        StaffSearchAction.setShortcut('Ctrl+9')
        StaffSearchAction.setStatusTip('Search Staff')
        StaffSearchAction.triggered.connect(self.render_staff_search_page)

        iconStaffContact = QtGui.QIcon('icons/contact2.png')
        StaffContactAction = QtGui.QAction(iconStaffContact, '&Contact', self)
        StaffContactAction.setShortcut('Ctrl+!')
        StaffContactAction.setStatusTip('Staff Contact info')
        StaffContactAction.triggered.connect(self.render_staff_contact_page)

        iconStaffD = QtGui.QIcon('icons/remove.png')
        StaffDAction = QtGui.QAction(iconStaffD, '&remove', self)
        StaffDAction.setShortcut('Ctrl+G')
        StaffDAction.setStatusTip('Staff Deletio')
        StaffDAction.triggered.connect(self.render_staff_delete_page)

        iconGranterRAction= QtGui.QIcon('icons/add3.png')
        GranterRAction = QtGui.QAction(iconGranterRAction, '&Grants', self)
        GranterRAction.setShortcut('Ctrl+y')
        GranterRAction.setStatusTip('Register Granter')
        GranterRAction.triggered.connect(self.render_granter_reg_page)

        iconGranterDAction= QtGui.QIcon('icons/remove2.png')
        GranterDAction = QtGui.QAction(iconGranterDAction, '&Remove', self)
        GranterDAction.setShortcut('Ctrl+%')
        GranterDAction.setStatusTip('Granter Removal')
        GranterDAction.triggered.connect(self.render_granter_delete_page)

        iconGranterSearchAction= QtGui.QIcon('icons/search.png')
        GranterSearchAction = QtGui.QAction(iconGranterSearchAction, '&Search', self)
        GranterSearchAction.setShortcut('Ctrl+5')
        GranterSearchAction.setStatusTip('Search Granter')
        GranterSearchAction.triggered.connect(self.render_granter_search_page)

        iconGranterContactAction= QtGui.QIcon('icons/contact2.png')
        GranterContactAction = QtGui.QAction(iconGranterContactAction, '&Contact', self)
        GranterContactAction.setShortcut('Ctrl+>')
        GranterContactAction.setStatusTip('Granter Contact Info')
        GranterContactAction.triggered.connect(self.render_granter_contact_page)

        iconAuthReg= QtGui.QIcon('icons/add.png')
        AuthReg = QtGui.QAction(iconAuthReg, '&Inscribe', self)
        AuthReg.setShortcut('Ctrl+M')
        AuthReg.setStatusTip('Register Author')
        AuthReg.triggered.connect(self.render_auth_reg_page)

        iconAuthRemoval= QtGui.QIcon('icons/remove2.png')
        AuthRemovalAction = QtGui.QAction(iconAuthRemoval, '&Remove', self)
        AuthRemovalAction.setShortcut('Ctrl+$')
        AuthRemovalAction.setStatusTip('Author Deletion')
        AuthRemovalAction.triggered.connect(self.render_auth_delete_page)

        iconAuthContact= QtGui.QIcon('icons/contact2.png')
        AuthContactAction = QtGui.QAction(iconAuthContact, '&Contact', self)
        AuthContactAction.setShortcut('Ctrl+H')
        AuthContactAction.setStatusTip('Author Contact Info')
        AuthContactAction.triggered.connect(self.render_auth_contact_page)

        iconAuthSearch= QtGui.QIcon('icons/search.png')
        AuthSearch = QtGui.QAction(iconAuthSearch, '&Search', self)
        AuthSearch.setShortcut('Ctrl+L')
        AuthSearch.setStatusTip('Search Author')
        AuthSearch.triggered.connect(self.render_auth_search_page)

        iconAuthCompile= QtGui.QIcon('icons/text.png')
        AuthCompile = QtGui.QAction(iconAuthCompile, '&Compile', self)
        AuthCompile.setShortcut('Ctrl+C')
        AuthCompile.setStatusTip('Compile Book')
        AuthCompile.triggered.connect(self.render_auth_comp_page)

        iconMemReg= QtGui.QIcon('icons/add3.png')
        MemberRegAction = QtGui.QAction(iconMemReg, '&Register', self)
        MemberRegAction.setShortcut('Ctrl+W')
        MemberRegAction.setStatusTip('Register Member')
        MemberRegAction.triggered.connect(self.render_mem_reg_page)

        iconMemPenalty= QtGui.QIcon('icons/attach.png')
        MemberPenaltyAction = QtGui.QAction(iconMemPenalty, '&Penalty', self)
        MemberPenaltyAction.setShortcut('Ctrl+W')
        MemberPenaltyAction.setStatusTip('Cancel or Check Penalty')
        MemberPenaltyAction.triggered.connect(self.render_mem_penalty_page)

        iconMemSearch= QtGui.QIcon('icons/risky.png')
        MemSearchAction = QtGui.QAction(iconMemSearch, '&Search', self)
        MemSearchAction.setShortcut('Ctrl+N')
        MemSearchAction.setStatusTip('Search Member')
        MemSearchAction.triggered.connect(self.render_mem_search_page)

        iconMemContact= QtGui.QIcon('icons/contact.png')
        MemContactAction = QtGui.QAction(iconMemContact, '&Contact', self)
        MemContactAction.setShortcut('Ctrl+Y')
        MemContactAction.setStatusTip('Member Contact Info')
        MemContactAction.triggered.connect(self.render_mem_contact_page)

        iconMemDelete= QtGui.QIcon('icons/remove.png')
        MemDeleteAction = QtGui.QAction(iconMemDelete, '&Remove', self)
        MemDeleteAction.setShortcut('Ctrl+J')
        MemDeleteAction.setStatusTip('Member Deletion')
        MemDeleteAction.triggered.connect(self.render_mem_delete_page)



        iconPubReg= QtGui.QIcon('icons/add3.png')
        PubRegAction = QtGui.QAction(iconPubReg, '&Register', self)
        PubRegAction.setShortcut('Ctrl+B')
        PubRegAction.setStatusTip('Register a Publisher')
        PubRegAction.triggered.connect(self.render_pub_reg_page)

        iconPubCont= QtGui.QIcon('icons/contact.png')
        PubContAction = QtGui.QAction(iconPubCont, '&Contact', self)
        PubContAction.setShortcut('Ctrl+C')
        PubContAction.setStatusTip('Publisher Contact Info')
        PubContAction.triggered.connect(self.render_pub_contact_page)

        iconPubDelete= QtGui.QIcon('icons/remove2.png')
        PubDeleteAction = QtGui.QAction(iconPubDelete, '&Remove', self)
        PubDeleteAction.setShortcut('Ctrl+&')
        PubDeleteAction.setStatusTip('Publisher Removal')
        PubDeleteAction.triggered.connect(self.render_pub_delete_page)

        iconPubSearch= QtGui.QIcon('icons/search.png')
        PubSearchAction = QtGui.QAction(iconPubSearch, '&Search', self)
        PubSearchAction.setShortcut('Ctrl+H')
        PubSearchAction.setStatusTip('Search a Publisher')
        PubSearchAction.triggered.connect(self.render_pub_search_page)

        iconBranchReg= QtGui.QIcon('icons/add2.png')
        BranchRegAction = QtGui.QAction(iconBranchReg, '&Register', self)
        BranchRegAction.setShortcut('Ctrl+L')
        BranchRegAction.setStatusTip('Register a Branch')
        BranchRegAction.triggered.connect(self.render_branch_reg_page)

        iconBranchSearch= QtGui.QIcon('icons/search.png')
        BranchSearchAction = QtGui.QAction(iconBranchSearch, '&Search', self)
        BranchSearchAction.setShortcut('Ctrl+2')
        BranchSearchAction.setStatusTip('Search a Branch')
        BranchSearchAction.triggered.connect(self.render_branch_search_page)

        iconBranchContact= QtGui.QIcon('icons/contact.png')
        BranchContactAction = QtGui.QAction(iconBranchContact, '&Contact', self)
        BranchContactAction.setShortcut('Ctrl+8')
        BranchContactAction.setStatusTip('Get Contact Info')
        BranchContactAction.triggered.connect(self.render_branch_contact_page)

        iconBranchD= QtGui.QIcon('icons/remove.png')
        BranchDAction = QtGui.QAction(iconBranchD, '&Remove', self)
        BranchDAction.setShortcut('Ctrl+W')
        BranchDAction.setStatusTip('Branch Deletion')
        BranchDAction.triggered.connect(self.render_branch_delete_page)

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
        menuBranch.addAction(BranchSearchAction)
        menuBranch.addAction(BranchContactAction)
        menuBranch.addAction(BranchDAction)

        menuPub.addAction(PubRegAction)
        menuPub.addAction(PubSearchAction)
        menuPub.addAction(PubContAction)
        menuPub.addAction(PubDeleteAction)

        menuMem.addAction(MemberRegAction)
        menuMem.addAction(MemberPenaltyAction)
        menuMem.addAction(MemSearchAction)
        menuMem.addAction(MemContactAction)
        menuMem.addAction(MemDeleteAction)

        menuAuth.addAction(AuthReg)
        menuAuth.addAction(AuthCompile)
        menuAuth.addAction(AuthSearch)
        menuAuth.addAction(AuthContactAction)
        menuAuth.addAction(AuthRemovalAction)

        menugranter.addAction(GranterRAction)
        menugranter.addAction(GranterSearchAction)
        menugranter.addAction(GranterContactAction)
        menugranter.addAction(GranterDAction)

        menustaff.addAction(StaffRAction)
        menustaff.addAction(StaffAAction)
        menustaff.addAction(StaffAReportAction)
        menustaff.addAction(StaffSearchAction)
        menustaff.addAction(StaffContactAction)
        if self.type=='Head':
            menustaff.addAction(StaffDAction)


        menuBook.addAction(RegisterBAction)
        menuBook.addAction(BorrowAction)
        menuBook.addAction(BorrowRetAction)
        menufile.addAction(exitAction)
    def render_absence_report_page(self):
        self.ins=StaffAbsenceReport(self.cur,self.type)
        self.ins.show()
    def render_branch_delete_page(self):
        self.ins=BranchDelete(self.cur,self.type)
        self.ins.show()

    def render_staff_delete_page(self):
        self.ins=StaffDelete(self.cur,self.type)
        self.ins.show()
    def render_mem_delete_page(self):
        self.ins=MemDelete(self.cur,self.type)
        self.ins.show()

    def render_pub_delete_page(self):
        self.ins=PubDelete(self.cur,self.type)
        self.ins.show()
    def render_granter_delete_page(self):
        self.ins=GranterDelete(self.cur,self.type)
        self.ins.show()
    def render_auth_delete_page(self):
        self.ins=AuthDelete(self.cur,self.type)
        self.ins.show()

    def render_staff_contact_page(self):
        self.ins=StaffContact(self.cur,self.type)
        self.ins.show()
    def render_auth_contact_page(self):
        self.ins=AuthContact(self.cur,self.type)
        self.ins.show()
    def render_pub_contact_page(self):
        self.ins=PubContact(self.cur,self.type)
        self.ins.show()

    def render_granter_contact_page(self):
        self.ins=GranterContact(self.cur,self.type)
        self.ins.show()

    def render_branch_contact_page(self):
        self.ins=BranchContact(self.cur,self.type)
        self.ins.show()

    def render_staff_search_page(self):
        self.ins=StaffSearch(self.cur,self.type)
        self.ins.show()
    def render_branch_search_page(self):
        self.ins=BranchSearch(self.cur,self.type)
        self.ins.show()
    def render_granter_search_page(self):
        self.ins=GranterSearch(self.cur,self.type)
        self.ins.show()
    def render_pub_search_page(self):
        self.ins=PubSearch(self.cur,self.type)
        self.ins.show()
    def render_auth_search_page(self):
        self.ins=AuthorSearch(self.cur,self.type)
        self.ins.show()
    def render_mem_contact_page(self):
        self.ins=MemContact(self.cur,self.type)
        self.ins.show()
    def render_mem_search_page(self):
        self.ins=MemberSearch(self.cur,self.type)
        self.ins.show()
    def render_staff_page(self):
        self.ins=StaffReg(self.cur,self.type)
        self.ins.show()
    def render_absence_page(self):
        self.ins_abs=StaffAbsence(self.cur,self.type)
        self.ins_abs.show()
    def render_book_page(self):
        self.d=BookReg(self.cur,self.type)
        self.d.show()
    def render_granter_reg_page(self):
        self.p=GranterReg(self.cur,self.type)
        self.p.show()
    def render_borrow_page(self):
        self.k=BookBorrow(self.cur,self.type)
        self.k.show()
    def render_borrow_return_page(self):
        self.isad=BookRetBorrow(self.cur,self.type)
        self.isad.show()
    def render_auth_reg_page(self):
        self.sds=AuthorRegister(self.cur,self.type)
        self.sds.show()
    def render_auth_comp_page(self):
        self.sd=Compile(self.cur,self.type)
        self.sd.show()
    def render_mem_reg_page(self):
        self.sp=MemberReg(self.cur,self.type)
        self.sp.show()
    def render_mem_penalty_page(self):
        self.pn=Penalty(self.cur,self.type)
        self.pn.show()
    def render_pub_reg_page(self):
        self.pb=PublisherReg(self.cur,self.type)
        self.pb.show()
    def render_branch_reg_page(self):
        self.br=BranchReg(self.cur,self.type)
        self.br.show()
def main():
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    app = QtGui.QApplication(sys.argv)
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QtGui.QIcon('icons/cr2.png'))
    loginDialog = Login()
    if loginDialog.exec_()==QtGui.QDialog.Accepted:
            ex = Main(loginDialog.ncur,loginDialog.nType)
            ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
