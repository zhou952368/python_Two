from DB import Db


class User:
    def __init__(self):
        self.phone_id = None
        self.Brand = None
        self.Price = None
        self.type = None
        self.quantity = None
        self.Version = None
        self.user = Db()

    # 手机录入
    def insert(self):
        self.phone_id = int(input("请输入手机编号:"))
        self.Brand = input("请输入手机的品牌:")
        self.type = input("请输入手机的型号:")
        self.Price = int(input("请输入手机的价格;"))
        self.quantity = int(input("请输入手机的数量:"))
        self.Version = input("请输入手机的版本:")
        self.user.insert_phone(self.phone_id, self.Brand, self.type, self.Price, self.quantity, self.Version)

    # 根据手机品牌查询手机信息
    def select(self):
        self.Brand = input("请输入手机品牌:")
        return self.user.select_phone(self.Brand)

    # 根据手机编号删除手机信息
    def delete(self):
        self.phone_id = int(input("请输入要删除的手机编号;"))
        self.user.delete_phone(self.phone_id)

    # 查询全部手机信息
    def select_all(self):
        return self.user.select_all()

    # 根据编号修改手机价格
    def update(self):
        self.phone_id = input("请输入手机编号;")
        self.Price = int(input("请输入手机新的价格:"))
        self.user.update_phone(self.phone_id, self.Price)


if __name__ == '__main__':
    user = User()
    user.insert()
    # user.delete()
    # print(user.select())
    # print(user.select_all())
    # user.update()