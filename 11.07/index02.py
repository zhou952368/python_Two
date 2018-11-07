import pymysql

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '952368'
PORT = '3306'
DB = 'python'
CHARSET = 'UTF8'


def affair():
    conn = pymysql.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        db=DB,
        charset=CHARSET
    )
    with conn.cursor() as cursor:
        try:
            conn.begin()
            sql1 = "select uid,username,price from user where uid= 1"
            cursor.execute(sql1)
            result = cursor.fetchone()
            money = result[2] - 500
            sql2 = "update user set price = %s where uid= 1" % (money)
            cursor.execute(sql2)
            sql3 = "select uid,username,price from user where uid= 2"
            cursor.execute(sql3)
            ziwie = cursor.fetchone()
            money = ziwie[2] + 500
            sql4 = "update user set price = %s where uid= 2" % (money)
            cursor.execute(sql4)
            conn.commit()
        except Exception as e:
            print(e)
            conn.collback()


if __name__ == '__main__':
    affair()
