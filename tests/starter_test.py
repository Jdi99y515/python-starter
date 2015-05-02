# -*- coding: utf-8 -*-
import pytest
from mock import patch

from starter import Starter
from starter.starter import main


def test_foo():
    s = Starter()
    result = s.foo()
    assert 'foo' == result


def test_bar():
    s = Starter()
    result = s.bar()
    assert 'bar' == result


def test_baz():
    s = Starter()
    result = s._baz('banana')
    assert 'baz' == result


def call_main(argv=None):
    with patch('sys.argv', argv):
        main()


def test_main_empty():
    call_main(['program_name'])


def test_main_foo():
    call_main(['program_name', '--foo'])


def test_main_bar():
    call_main(['program_name', '--bar', 'BAR'])


def test_main_version():
    with pytest.raises(SystemExit):
        call_main(['program_name', '--version'])


def test_main_help():
    with pytest.raises(SystemExit):
        call_main(['program_name', '--help'])
