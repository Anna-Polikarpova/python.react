import time


class cntxMng():
    def __init__(self):
        self.start = time.time()

    def __enter__(self, *args):
        return

    def __exit__(self, *args):
        print('Затрачено: {}'.format(time.time() - self.start))


with cntxMng():
    time.sleep(0.5)