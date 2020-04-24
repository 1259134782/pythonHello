# -*- coding: utf-8 -*-

import time


class HelloForTest(object):
    def __init__(self):
        self._create_ticks = time.time()
        pass

    def SayHello(self):
        print self._create_ticks
        pass


if __name__ == "__main__":
    hft = HelloForTest()
    hft.SayHello()
