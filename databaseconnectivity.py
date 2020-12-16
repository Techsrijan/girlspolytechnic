import pymysql
connection=pymysql.connect(host="localhost",user="root",db="girlspoly")
mycursor=connection.cursor()
print("connection established")
'''sqlque="Create table login (name varchar(22),age int(4))"
mycursor.execute(sqlque)
'''
'''queins="insert into login(name,age) values('ram',25)"
mycursor.execute(queins)
'''

'''name="rohan"
age="55"
queins="insert into login(name,age) values(%s,%s);"
val=(name,age)
mycursor.execute(queins,val)
'''

name="Ramesh"
updateque="update login set name=%s where age=55"
val=(name)
mycursor.execute(updateque,val)



connection.commit() # it is necessary step to save data permanently
connection.close()