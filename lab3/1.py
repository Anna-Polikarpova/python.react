goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'color': 'black'}]
import random


def gen_random(Num, start, finish):
    for i in range(Num):
        yield (random.randrange(start, finish))


print([i for i in gen_random(4, 2, 7)])


def field(list, *args):
    for l in list:
        if len(args) > 1:
            for a in args:
                if a in l.keys():
                    if l[a] is not None:
                        yield l[a]
        elif len(args) == 1:
            for a in args:
                if a in l.keys():
                    if l[a] is not None:
                        yield l[a]

print("field:", [i for i in field(goods, 'title','price')])