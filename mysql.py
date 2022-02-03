import pymysql

connection = pymysql.connect(host="localhost", user="root", password="bonjouroumar200", db="py", port=3306,
                             charset="utf8")
cursor = connection.cursor()

# cursor.execute("create table student(studentId int(10) primary key, name varchar(20), sex varchar(10), age int(10), "
#                "class varchar(10), major varchar(20))")
cursor.execute(
    'insert into student(studentId,name,sex,age,class, major)values(100140, "al","male",32,"3171","anglais "),'
    '(1001423, "sow","male",22,"3171","software "), (100142, "siallo","male",16,"3171","mechanic "),(100146, "Alpha",'
    '"male",13,"3171","software "),(100141, "Alpha","male",12,"3171","engineering "),(10015, "sow","male",23,"3171",'
    '"software "),(10014, "Alpha","male",22,"3171","economis "), (1001312,"Alpha","male",22,"3171","software"),'
    '(10013, "Alpha","male",22,"3171","software " ),(1002, "Alphaoumar","male",22,"3171","software " ),(1003, '
    '"Alphadiallo","male",22,"3172","software " ),(1004, "Alphayou","male",22,"3173","software " ),(1005, "Alphame",'
    '"male",22,"3174","software " ), (1006, "Alphaand","female",22,"3176","soft " ),(1008, "Alphabarry","male",22,'
    '"3178","soft " ), (1009, "Alphabalde","male",22,"3179","soft " )')
# cursor.execute("select * from student")
# alp = cursor.execute("select * from student where sex='male'")
# cursor.execute("select count(*) from student group by major")
# cursor.execute("delete  from student where stu_id=1")
connection.commit()
result = cursor.fetchall()

# print(result)
# print(alp)
cursor.close()
connection.close()

# 1.通过mysql创建数据库mydb；编写python程序，在数据库中创建表Student，
# 并且添加3条以上数据。表字段名及类型如下：
# stu_id  CHAR(10)；stu_name  CHAR(20), stu_age  INT, 
# stu_sex  CHAR(1), stu_ score FLOAT。

# THE ANSWER

# connection = pymysql.connect(
#   host="localhost",user="root",password="bonjouroumar200",
#   db="mydb",port=3306,charset="utf8")
# cursor = connection.cursor()
# cursor.execute("create table student(studentId varchar(10) primary key,stu_name varchar(20), stu_sex varchar(10), stu_age int(10), stu_score float(10))")
# cursor.execute('insert into student(studentId,name,sex,age,class, major)values("1001423", "sow","male",22,"3171","software "))
# cursor.execute("select * from student")
# cursor.execute("delete  from student where stu_id='20180101'")
