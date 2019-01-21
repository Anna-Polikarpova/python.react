data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

class Unique:
    def __init__(self,lst,ignore_case=False):
        self.data = self.new_list(data,ignore_case)
        self.n = len(self.data)
        self.i = 0

    def  __iter__(self):
        return self

    def new_list(self, l, ignore_case):
        new_lst = []
        if ignore_case:
            l = [i.lower() for i in l]
        for el in l:
            if el in new_lst:
                continue
            else:
                new_lst.append(el)
        return new_lst

    def __next__(self):
        if self.i < self.n:
            ret = self.data[self.i]
            self.i += 1
            return ret
        else:
            raise StopIteration()

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
x = Unique(data)
print([i for i in x])