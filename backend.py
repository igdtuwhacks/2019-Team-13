import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer, des text, certi text, logo text, orgname text, orgadd text, start Date, min integer, max integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn,des,certi,logo,orgname,orgadd,start,min,max):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)",(title,author,year,isbn,des,certi,logo,orgname,orgadd,start,min,max))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn="",des="",certi="",logo="",orgname="",orgadd="",start="",min="",max=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? OR des=? OR certi=? OR logo=? OR orgname=? OR orgadd=? OR start=? OR min=? OR max=?", (title,author,year,isbn,des,certi,logo,orgname,orgadd,start,min,max))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?, des=?, certi=?, logo=?, orgname=?, orgadd=?, start=?, min=?, max=? WHERE id=?",(title,author,year,isbn,des,certi,logo,orgname,orgadd,start,min,max,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
