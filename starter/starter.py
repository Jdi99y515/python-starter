#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
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
    
    parser.add_argument('-f', '--foo', action='foo', default='Foo', help='Foo')
    parser.add_argument('-b', '--bar', dest='bar', default=None, help='Bar')

    args, _ = parser.parse_known_args()

    s = Starter()

    if args.foo:
        s.foo()

    elif args.bar:
        s.bar()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
