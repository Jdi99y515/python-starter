# python-starter

[![Circle CI](https://circleci.com/gh/sroberts/python-starter.svg?style=svg)](https://circleci.com/gh/sroberts/python-starter)

A starter template for building a Python package.

Based on @ivanlei's fantastic [threatbutt](https://github.com/ivanlei/threatbutt) Maltego Plugins.

# virtualenv
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is a fantastic tools for creating python environments. To easily create and use the python-starter virtualenv:
```shell
$ make venv
```

To begin using the virtualenv:
```shell
$ source venv*/bin/activate
```

The packages installed into the virtualenv are dictated by two files
### `requirements.txt`
In this file, all packages required to run the tool should be listed. Specify the exact version of the packages so that changes in dependencies don't break your tool.
### `requirements-dev.txt`
In this file, additional packages required to test the tool should be listed. Generally, the exact version is not specified.

# unit testing
Unit testing is at the very heart of making code work. Use the pytest framework and add tests to the `tests/` directory. To run tests:
```shell
$ make test
```

# code coverage
Code coverage is a testing tool that helps identify which lines of code are executed during unit testing and which aren't. Untested lines of code are bugs waiting to happen. The `coverage` code coverage tool runs each time you `make test`

# pre-commit
[pre-commit](http://pre-commit.com) is a tool to find and fix common issues before changes are committed. `pre-commit` will run before each `git commit`.
To run `pre-commit` on demand:
```shell
$ pre-commit run -a
```

# running your code
Writing code is great. But running it is usually the end goal. In `setup.py` the `entry_points` section defines command-line entry points for running your code. Inside your virtualenv, run:
```shell
$ starter
```

# versioning your code
There is a single definition of the package version in `starter/__init__.py`. Updating there changes the package version.

# pypi
pypi is a wonderous server that will let your package be installed with:
```shell
$ pip install starter
```

The list of packages in `requirements.txt` needs to be repeated in the `install_requires` section of `setup.py` if your package will be hosted on pypi.

To get a package hosted on pypi:
1. Register your project to PyPI. It's an one time only operation.
```shell
$ python setup.py register
```

2. Package your source for distribution. In a virtual enviroment install [wheel](https://pypi.python.org/pypi/wheel) and [twine](https://pypi.python.org/pypi/twine):
```shell
$ pip install wheel twine
```

3. Create a source distribution. First build the tarball package:
```shell
$ python setup.py sdist
```

4. Then build the wheel. A [wheel](https://packaging.python.org/en/latest/distributing.html#pure-python-wheels) is a zip-format archive specially formatted for packaging:
```shell
$ python setup.py bdist_wheel
```
The commands `sdist` and `bdist_wheel` use the package version number registered in the `setup.py` file to create packages under a folder named `./dist`

5. Upload to PyPI with the credentials you have in `~/.pypirc` (from step 2). We use `twine` to send this data through an encrypted channel:
```shell
$ twine upload dist/*
```

6. Observe your work at http://pypi.python.org/pypi/<project name>. You should be able to `pip install` your project now.
