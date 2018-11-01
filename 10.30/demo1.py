import time


def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        return endTime - startTime

    return wrapper


@deco
def fun():
    for i in range(1, 100000000):
        if i == 99999999:
            return i


if __name__ == '__main__':
    f = fun
    print(f())
