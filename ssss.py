import cx_Oracle
connection=cx_Oracle.connect("scott/tiger@192.168.0.106")
cursor1=connect.cursor()
rsesult=cursor1.execute("select * from emp")