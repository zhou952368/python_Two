import pymysql


class Db:

    def __init__(self):
        self.db = pymysql.connect("127.0.0.1", "root", "952368", "python", charset='utf8')
        self.cursor = self.db.cursor()

    def insert_phone(self, ID, Brand, type, Price, quantity, Version):
        sql = 'insert into phone(ID, Brand, type, Price, quantity, Version) value (%s,%s,%s,%s,%s,%s)'
        try:
            # 执行sql插入语句
            self.cursor.execute(sql, (ID, Brand, type, Price, quantity, Version))
            # 提交到数据库执行
            self.db.commit()
            print("添加成功")
        except Exception as e:
            print(e)

    def delete_phone(self, phone_id):
        sql = 'delete from phone where id = "{0}" '.format(phone_id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("删除成功")
        except Exception as e:
            print(e)

    def select_phone(self, brand):
        sql = 'select * from phone where Brand = "{0}"'.format(brand)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def select_all(self):
        sql = 'select * from phone'
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def update_phone(self, phone_id, price):
        sql = 'update phone set Price = %s where ID = %s' % (price, phone_id)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("更新成功")
        except Exception as e:
            print(e)
        self.db.close()