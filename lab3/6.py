import json
import time
from random import randint

class cntxMng():
    def __init__(self):
        self.start = time.time()

    def __enter__(self, *args):
        return

    def __exit__(self, *args):
        print('Затрачено: {}'.format(time.time() - self.start))


def print_result(foo):
    def decorated(arg):
        print(foo.__name__)
        fr = foo(arg)
        if isinstance(fr, list):
            print('\n'.join(list(map(str, fr))))
        elif isinstance(fr, dict):
            print('\n'.join(["{} = {}".format(key, value) for key, value in fr.items()]))
        return fr

    return decorated


with open("data_light.json", encoding="utf - 8") as f:
    data = json.load(f)


@print_result
def f1(*args):
    return sorted(list(set([data[prof_el]["job-name"].lower() for prof_el in range(len(data))])))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x+' с опытом Python',arg))


@print_result
def f4(arg):
    money = randint(10**5,2*10**5)
    return list(map(lambda x: x+',зарплата '+str(money)+' руб',arg))


with cntxMng():
    time.sleep(0.5)
    print(type(f2(f1(data))))
    f4(f3(f2(f1(data))))