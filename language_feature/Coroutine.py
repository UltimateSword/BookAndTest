def consumer():
    r = ''  # 声明变量
    while True:
        n = yield r  # 声明接受值
        if not n:
            return
        print('consumer {}'.format(n))
        r = '200 ok'


def producer(c):
    c.send(None)  # coroutine start
    for n in range(1, 5):
        print('producer {}'.format(n))
        res = c.send(n)
        print('consumer return {}'.format(res))
    c.close()


if __name__ == '__main__':
    c = consumer()
    producer(c)
