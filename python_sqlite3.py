#! /home/yushun/anaconda3/bin/python
import sqlite3

def init(path):
    con = sqlite3.connect(path)
    return con

def create(con,tables):
    cur = con.cursor()
    for table in tables:
        SQL = "CREATE TABLE "+ table +"(title,year,score)"
        cur.execute(SQL)
    return cur

def insert(cur,table,contexts):
    for context in contexts:
        SQL = "INSERT INTO " + table + " VALUES (" + context +")"
        cur.execute(SQL)

def select(cur,tables):
    result = []
    for table in tables:
        SQL = "SELECT * FROM " +table
        result.append(cur.execute(SQL).fetchall())
    return result

def translate_table(tables):
    table_list = []
    for table in tables:
        table_list.append(table[0])
    return table_list

def comp_list_num(list0,list1):
    if len(list0) < len(list1):
        return len(list0)
    else:
        return len(list1)

def comp_col(col0,col1):
    col_num = comp_list_num(col0,col1)
    for i in range(col_num):
        if col0[i] != col1[i]:
            print("\n\n***********************")
            print(col0[i])
            print(col1[i])
            return True

def comp_row(row0,row1):
    row_num = comp_list_num(row0,row1)
    row_diff = []
    for i in range(row_num):
        if comp_col(row0[i],row1[i]):
            print("--------------------------")
            print(row0[i])
            print(row1[i])
            print("--------------------------")
            row_diff.append(i)
    return row_diff

def comp_table(db0,db1):
    table_num = comp_list_num(db0,db1)
    for i in range(table_num):
        row_diff = comp_row(db0[i],db1[i])
        if len(row_diff) != 0:
            print("table name :")
            print(tables0[i])

if __name__ == "__main__":
    con0 = init("./tutorial0.sqlite")
    con1 = init("./tutorial1.sqlite")
    cur0 = con0.cursor()
    cur1 = con1.cursor()

    tables0 = cur0.execute("SELECT name FROM sqlite_master")
    tables1 = cur1.execute("SELECT name FROM sqlite_master")
    tables0 = translate_table(tables0.fetchall())
    tables1 = translate_table(tables1.fetchall())
    result0 = select(cur0,tables0)
    result1 = select(cur1,tables1)
    comp_table(result0,result1)

