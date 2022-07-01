import heapq
import sys


class Test:
    temp_node = 'auuu?'

    def temp_node_cng(self):
        # nonlocal temp_node
        print(f'print from temp_node_test func. {temp_node=}')
        temp_node = 'QQ!'
        print(f'print from temp_node_test func. {temp_node=}')

    def test2(self):
        print(f'print from test2 func. {temp_node=}')


def decorate(funct):
    def wrapper(param1):
        print('декоратор вызван')
        funct(param1)
    return wrapper


@decorate
def t(param):
    print(param)

def fix(b, s=set()):
    s.add(b)
    print(s)

if __name__ == '__main__':
    # temp_node = 'auuu?'
    # t = Test()
    # t.temp_node_cng()
    # t.test2()
    # t("тест QQ!")
    fix(3)
    fix(4, {6, 5})
    fix(2)