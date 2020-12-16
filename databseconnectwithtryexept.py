import pymysql

try:
    conn=pymysql.connect(host="localhost",user="root",db="girlspoly")
    mycursor=conn.cursor()
    sqlque="select * from login"
    mycursor.execute(sqlque)
    records = mycursor.fetchall()
    print(records)
    for row in records:
        print("Id=",row[0])
        print("Name = ", row[1] )
        print("age = ", row[2],"\n")
except ValueError as e:
    print("Error while connecting to MySQL", e)
finally:
   conn.close()
   print("MySQL connection is closed")