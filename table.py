__author__ = 'soheil'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

################################################### BOOK TABLES
class sTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

        #\self.resizeRowsToContents()

    def setmydata(self):



        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                #newitem.setText(QString(str(self.data[i][j])))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['Bid','ISBN','Title','Subject','pub_date','price','branch_id','publisher_id','num_published','granter_id','granted_date','borrow_mem_id','borr_due_date','borr_return_date','Available'])



class AuthTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

        #\self.resizeRowsToContents()

    def setmydata(self):



        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                #newitem.setText(QString(str(self.data[i][j])))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['Title','AuthorFname','AuthorLname'])




########################################### MEMBER TABLES


class MemTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['ID','Fname','Lname','MemShipDate','ExpDate','SSN','country','city','district','street','alley','buildingNo','postalCode','branchID','Type','Penalty'])

###########################################AUTHOR


class AuthorTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['ID','Fname','Lname',])

#########################Publisher



class PublisherTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['ID','Name','country','city','district','street','alley','buildingNo','postalCode'])

################################################# Granter

class GranterTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['ID','Fname','Lname','SSN','country','city','district','street','alley','buildingNo','postalCode'])

######################################## BranchTable

class BranchTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['ID','Name','HeadID','city','district','street','alley','buildingNo','postalCode'])

##################################################### Staff Table
class StaffTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.rows=len(self.data)
        self.cols=len(self.data[0])
        self.setColumnCount(self.cols)
        self.setRowCount(self.rows)
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()


    def setmydata(self):

        for i in range(self.rows):
            for j in range(self.cols):
                newitem = QTableWidgetItem(str(self.data[i][j]))
                self.setItem(i,j,newitem)
        self.setHorizontalHeaderLabels(['ID','BranchID','Fname','Lname','EmpDate','SSN','City','District','street','alley','buildingNo','postalCode','salary','StaffType'])