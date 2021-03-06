#!/usr/bin/env python
# -*- coding: utf8 - *-
"""cihai-cli lives at <https://cihai-cli.git-pull.com>."""

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

about = {}
with open("cihai_cli/__about__.py") as fp:
    exec(fp.read(), about)

with open('requirements/base.txt') as f:
    install_reqs = [line for line in f.read().split('\n') if line]

with open('requirements/test.txt') as f:
    tests_reqs = [line for line in f.read().split('\n') if line]

if sys.version_info[0] > 2:
    readme = open('README.rst', encoding='utf-8').read()
else:
    readme = open('README.rst').read()

history = open('CHANGES').read().replace('.. :changelog:', '')


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__github__'],
    download_url=about['__pypi__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__email__'],
    description=about['__description__'],
    long_description=readme,
    packages=['cihai_cli'],
    include_package_data=True,
    install_requires=install_reqs,
    tests_require=tests_reqs,
    cmdclass={'test': PyTest},
    zip_safe=False,
    keywords=about['__title__'],
    entry_points=dict(console_scripts=['cihai=cihai_cli.cli:cli']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: System :: Shells",
        "Topic :: Utilities",
    ],
)
