# -*- coding: utf-8 -*-
import sys


class MetaPathFinder:

    def find_module(self, fullname, path=None):
        print('find_module {}'.format(fullname))
        return MetaPathLoader()


class MetaPathLoader:

    def load_module(self, fullname):
        print('load_module {}'.format(fullname))
        sys.modules[fullname] = sys
        return sys

sys.meta_path.insert(0, MetaPathFinder())

if __name__ == '__main__':
    import http
    print(http)
    print(http.version_info)
