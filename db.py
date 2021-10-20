import sqlite3
from sqlite3 import Error

def conectar():
    dbname= 'pedidos.db'
    conn= sqlite3.connect(dbname)
    return conn

def getProductos():
    conn= conectar()
    cursor= conn.execute("select * from Producto;")
    resultados= list(cursor.fetchall())
    conn.close()
    return resultados

def addProducto(producto, valor, cantidad):
    try :
        conn=conectar()
        conn.execute("insert into Producto (nombre, precio, existencia) values(?,?,?);", (producto, valor, cantidad))
        conn.commit()
        conn.close()
        return True
    except Error as error:
        print(error)
        return False

def getProducto(id):
    try : 
        conn= conectar()
        SQLstmt="select * from Producto where id="+str(id)+";"
        print(SQLstmt)
        cursor= conn.execute(SQLstmt)
        #cursor= conn.executescript(SQLstmt)
        resultado= cursor.fetchall()
        return resultado
    except Error as error:
        return error



def getProductoSecure(id):
    try : 
        conn= conectar()
        t= (id)
        SQLstmt="select * from Producto where id=?;"
        cursor= conn.execute(SQLstmt,  (id,))
        resultado= cursor.fetchall()
        return resultado
    except Error as error:
        return error

if __name__=='__main__':
    getProducto('1; select * from Cliente')


