#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

__version__ = '0.0.1'


class Starter(object):

    """A Starter object."""

    def __init__(self):
        pass

    def foo(self):
        return "foo"

    def bar(self):
        return "bar"

    def _baz(self, text):
        return "baz"


def main():
    """
    It's main!
    """

    parser = ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s (version {0})'.format(__version__))
    parser.add_argument('-f', '--foo', dest='foo', default=False, action='store_true', help='Foo')
    parser.add_argument('-b', '--bar', dest='bar', default='', help='Bar')

    args, _ = parser.parse_known_args()

    s = Starter()

    if args.foo:
        result = s.foo()
        print result

    elif args.bar:
        result = s.bar()
        print result

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
