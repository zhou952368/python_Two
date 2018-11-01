def a(func):
    dic = {"zhou": "952368", "feng": "952368"}

    def b(*args, **kwargs):
        if user in dic.keys():
            if password == dic[user]:
                func(*args, **kwargs)
                return "登录成功"
        return "账号或者密码有误,请重新输入"

    return b


@a
def fun(user, password):
    pass


if __name__ == '__main__':
    f = fun
    user = input("请输入你的用户名:")
    password = input("请输入你的密码:")
    print(f(user, password))
