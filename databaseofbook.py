
import pymysql

con = None
cur = None

def dbconnect():
    global con,cur
    con = pymysql.connect(host='localhost',
                           database='library_management',
                           user='root',
                           password='')


    cur = con.cursor()

def dbdisconnect():
    cur.close()
    con.close()

def insertbook(id,name,author_name,price,type):
    try:
        dbconnect()
        sql = f'insert into books values({id},"{name}","{author_name}",{price},"{type}")'
        cur.execute(sql)
        con.commit()
        return "Adding books successful"
    except Exception as e:
        return e
    finally:
        dbdisconnect()

def updatebook(data):
    try:
        dbconnect()
        sql = f'update books set name="{data[1]}",price={data[3]},author_name="{data[2]}",type="{data[4]}" where id = {data[0]}'
        cur.execute(sql)
        con.commit()
        return 'Book updated successfully'
    except Exception as e:
        return e 
    finally:
        dbdisconnect()
    

def deletebook(id):
    try:
        dbconnect()
        sql = f'delete from books where id={id}'
        cur.execute(sql)
        con.commit()
        return'Delete book successful'
    except  Exception as e:
        return e 
    finally:
        dbdisconnect()

def returnbook(stuid,ID,name,issuedate,returndate):
    try:
        dbconnect()
        sql = f'insert into returnb values({stuid},{ID},"{name}","{issuedate}","{returndate}")'
        cur.execute(sql)
        con.commit()
        return "Return book successful"
    except Exception as e:
        return e 
    finally:
        dbdisconnect()   

def issuebook(stuid,stuname,ID,name,issuedate):
    try:
        dbconnect()
        sql = f'insert into studentb values({stuid},"{stuname}",{ID},"{name}","{issuedate}")'
        cur.execute(sql)
        con.commit()
        return "Issue book successful"
    except Exception as e:
        return e 
    finally:
        dbdisconnect()
def showbook():
    dbconnect()
    sql = 'select * from books'
    cur.execute(sql)
    data = cur.fetchall()
    return data
    dbdisconnect()

def searchbook(id):
    dbconnect()
    sql = f'select * from books where id = {id}'
    cur.execute(sql)
    data = cur.fetchone()
    dbdisconnect()
    return data

def showissuebook():
    dbconnect()
    sql = 'select * from studentb'
    cur.execute(sql)
    data = cur.fetchall()
    return data
    dbdisconnect()

def showreturnbook():
    dbconnect()
    sql = 'select * from returnb'
    cur.execute(sql)
    data = cur.fetchall()
    return data
    dbdisconnect()