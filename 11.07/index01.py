import pymysql

HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '952368'
PORT = '3306'
DB = 'python'
CHARSET = 'UTF8'


def insert_table():
    conn = pymysql.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        db=DB,
        charset=CHARSET
    )
    with conn.cursor() as cursor:
        values = [str(item) for item in range(20, 30)]
        sql = "insert into phone(id) value (%s)"
        cursor.executemany(sql, values)
        conn.commit()


if __name__ == '__main__':
    insert_table()
