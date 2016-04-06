# -*- coding: utf-8 -*-
import functools
import time


def func_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start func')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('spent {}s'.format(end - start))
        return result
    return wrapper


def sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    func = func_wrapper(sleep)
    print(func(3))
