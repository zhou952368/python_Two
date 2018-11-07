import pymysql

'''
1.连接数据库
 ip地址  端口 用户名  密码 数据库 编码集
2.建立游标
3.执行sql语句
4.处理数据
5.关闭数据库
'''
db = pymysql.connect('127.0.0.1', 'root', '952368', 'python', charset='utf8')
cursor = db.cursor()
sql = "SELECT * from emp"
try:
    cursor.execute(sql)
    date = cursor.fetchall()
    for i in date:
        empno = i[0]
        ename = i[1]
        print(empno, ename)
except Exception as e:
    print(e)
cursor.close()
db.close()
