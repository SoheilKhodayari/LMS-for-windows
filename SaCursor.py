__author__ = 'soheil'
import pypyodbc
connection_string ='Driver={SQL Server};Server=T2SOHEIL\T2SOHEIL;Database=LIBRARY;Uid=sa;Pwd=soheil9759865;'
c = pypyodbc.connect(connection_string)
cur=c.cursor()
type='sa'



def changeConnection(username):
    global connection_string
    global c
    global cur
    global type
    cur.execute('select staff_type from staff where staff_id='+username)
    staff_type=cur.fetchall()[0][0]
    if staff_type==1:
        connection_string ='Driver={SQL Server};Server=T2SOHEIL\T2SOHEIL;Database=LIBRARY;Uid=sa;Pwd=soheil9759865;'
        #connection_string ='Driver={SQL Server};Server=T2SOHEIL\T2SOHEIL;Database=LIBRARY;Uid=Head;Pwd=master;'
        c = pypyodbc.connect(connection_string)
        cur=c.cursor()
        type='Head'
    elif staff_type==0:
        connection_string ='Driver={SQL Server};Server=T2SOHEIL\T2SOHEIL;Database=LIBRARY;Uid=sa;Pwd=soheil9759865;'
        #connection_string ='Driver={SQL Server};Server=T2SOHEIL\T2SOHEIL;Database=LIBRARY;Uid=Secretary;Pwd=sec;'
        c = pypyodbc.connect(connection_string)
        cur=c.cursor()
        type='Secretary'
    return (type,cur)



