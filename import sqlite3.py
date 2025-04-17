import sqlite3
conn=sqlite3.connect("sales_data.db")
cursor=conn.cursor()
# create sales table data
cursor.execute(""" create table if not exists sales(id integer primary key,product text,quantity integer,price real)""")
conn.commit()
sales_data=[(1,'samsung',10,20000),
            (2,'apple',9,40000),
            (3,'vivo',14,25000),
            (4,'nokia',19,26000),
            (5,'realme',5,10000),
            (6,'vivo',7,22000),
            (7,'nothing',6,24000),
             (8,'redmi',10,27000),
                (9,'oppo',12,29000),
                (10,'one plus',13,23000)]
cursor.executemany("insert into sales(id,product,quantity,price) values(?,?,?,?)",sales_data)
conn.commit()
cursor.execute("select* from sales")
for row in cursor.fetchall():
    print(row)
